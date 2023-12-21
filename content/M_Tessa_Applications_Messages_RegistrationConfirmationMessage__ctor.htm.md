# RegistrationConfirmationMessage - конструктор
Initializes a new instance of the
[RegistrationConfirmationMessage](T_Tessa_Applications_Messages_RegistrationConfirmationMessage.htm)
class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Messages](N_Tessa_Applications_Messages.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public RegistrationConfirmationMessage(
    	int processId,
    	[NotNullAttribute] string applicationInstanceServiceAddress
    )
VB __Копировать
     Public Sub New ( 
    	processId As Integer,
    	<NotNullAttribute> applicationInstanceServiceAddress As String
    )
C++ __Копировать
     public:
    RegistrationConfirmationMessage(
    	int processId, 
    	[NotNullAttribute] String^ applicationInstanceServiceAddress
    )
F# __Копировать
     new : 
            processId : int * 
            [<NotNullAttribute>] applicationInstanceServiceAddress : string -> RegistrationConfirmationMessage
#### Параметры
processId [Int32](https://learn.microsoft.com/dotnet/api/system.int32)
     Идентификатор процесса 
applicationInstanceServiceAddress
[String](https://learn.microsoft.com/dotnet/api/system.string)
     Адрес подключения к сервису экземпляра приложения 
## __См. также
#### Ссылки
[RegistrationConfirmationMessage -
](T_Tessa_Applications_Messages_RegistrationConfirmationMessage.htm)
[Tessa.Applications.Messages - пространство
имён](N_Tessa_Applications_Messages.htm)
