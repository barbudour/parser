# CardRequestTypes.MailSent - поле
Запрос на выполнение обработки после успешной отправки письма. В этом случае
обычно выполняется очистка, в т.ч. для приложенных файлов, если они
формировались динамически. В объекте
[Info](P_Tessa_Cards_CardInfoStorageObject_Info.htm) содержатся параметра
отправленного письма: MailInfo \- сериализованный объект
[MailInfo](T_Tessa_Notices_MailInfo.htm); Email \- один или несколько почтовых
адресов, на которые было отправлено письмо; Subject \- тема письма; Body \-
тело письма, обычно в формате HTML.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static readonly Guid MailSent
VB __Копировать
     Public Shared ReadOnly MailSent As Guid
C++ __Копировать
     public:
    static initonly Guid MailSent
F# __Копировать
     static val MailSent: Guid
#### Значение поля
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __См. также
#### Ссылки
[CardRequestTypes - ](T_Tessa_Cards_CardRequestTypes.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
