odoo.define('wamy_website.validation_email',function(require){
    'use strict';
    var publicWidget = require('web.public.widget');
    var fields_phone = [];
    publicWidget.registry.wamy_website_email = publicWidget.Widget.extend({
        selector: '.schoolarship',
        events: {
             'change input[name="email"]':'_onChangeEmail',
             'change input[type="email"]':'_onChangeEmailRe',
			 'change input[type="tel"]':'_onChangetel',
		     'click': '_onClick',
             

        },

       _onChangeEmail :function(ev){
            var self = this;
			console.log("======>On change email====>")
            var $error=this.$('.email_student')
            var email =  self.$('[name="email"]').val();
            var $btn = this.$('.sign_up_partner');
            var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

            if (email !=''){
            if (!re.test(String(email).toLowerCase()))  {
               $('#errormail').show()
               $error.addClass('error-student')
               ev.target.setCustomValidity('يرجى ملء هذا الحقل ');
             $btn.attr('disabled', 'disabled');
            }
            else{
                $('#errormail').hide()
                 $error.removeClass('error-student')

            }
            }
             else{
                $('#errormail').hide()
                 $error.removeClass('error-student')
            }

       },





       _onChangetel :function(ev){


            var self = this;
            var $error=$(ev.currentTarget) 
            var mobile =  $(ev.currentTarget).val();

            var inputtexeterror=$(ev.currentTarget).parent().find('div#errormobile');


            var $btn = this.$('.sign_up_partner');
            var $ajout = this.$('.ajout');


            if (mobile !=''){

            if (isNaN(mobile))  {
               inputtexeterror.show()
               $error.addClass('error-student')
                 ev.target.setCustomValidity('يرجى ملء هذا الحقل ');

                    if ($error.hasClass('email_studentr'))
                    {    $ajout.addClass('error-relative');
                        $error.addClass('error-relative-std');


                        ev.target.setCustomValidity('يرجى ملء هذا الحقل ');
                 }


            }
            else{

                inputtexeterror.hide()
               $error.removeClass('error-student')
                 $ajout.removeClass('error-relative')
                  $error.removeClass('error-relative-std');
            }
            }
             else{

                inputtexeterror.hide()
                $error.removeClass('error-student')
                 $ajout.removeClass('error-relative')
                  $error.removeClass('error-relative-std');
            }


        },
       _onChangeEmailRe :function(ev){

            var self = this;
            var $error=$(ev.currentTarget) //this.$('.email_studentr')
            var email =  $(ev.currentTarget).val();

            var inputtexeterror=$(ev.currentTarget).parent().find('div#errormail1');


            var $btn = this.$('.sign_up_partner');
            var $ajout = this.$('.ajout');

            var re = /^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
            if (email !=''){
            if (!re.test(String(email).toLowerCase()))  {
               inputtexeterror.show()
               $error.addClass('error-student')
                

                    if ($error.hasClass('email_studentr'))
                    {    $ajout.addClass('error-relative');
                        $error.addClass('error-relative-std');
                        ev.target.setCustomValidity('يرجى ملء هذا الحقل ');
                 }
            }
            else{

                inputtexeterror.hide()
               $error.removeClass('error-student')
                 $ajout.removeClass('error-relative')
                  $error.removeClass('error-relative-std');
            }
            }
             else{

                inputtexeterror.hide()


                $error.removeClass('error-student')
                 $ajout.removeClass('error-relative')
                  $error.removeClass('error-relative-std');

            }


        },

  _onPublishBtnClick: function (ev) {//        ev.preventDefault();
        if (document.body.classList.contains('editor_enable')) {
           return;
        }

        var self = this;
       var $data = $(ev.currentTarget).parents(".js_publish_management:first");
       this._rpc({
            route: $data.data('controller') || '/student_schoolarship/detail',
           params: {
	           id: +$data.data('id'),
               object: $data.data('object'),
           },
        })
         .then(function (result) {
           $data.toggleClass("unpublished published");
            $data.find('input').prop("checked", result);
            $data.parents("[data-publish]").attr("data-publish", +result ? 'on' : 'off');
            if (result) {
                self.displayNotification({
                    type: 'success',
                    message: $data.data('description') ?
                        _.str.sprintf(_t("You've published your %s."), $data.data('description')) :
                       _t("Published with success."),
                });
            }    
   })
           .guardedCatch(function (err, data) {
           data = data || {statusText: err.message.message};
            return new Dialog(self, {
               title: data.data ? data.data.arguments[0] : "",
                $content: $('<div/>', {
                    html: (data.data ? data.data.arguments[1] : data.statusText)
                        + '<br/>'
                        + _.str.sprintf(
                            _t('It might be possible to edit the relevant items or fix the issue in <a href="%s">the classic Odoo interface</a>'),
                            '/web#model=' + $data.data('object') + '&id=' + $data.data('id')
                        ),
                }),
            }).open();
        });


    },


        });


         })