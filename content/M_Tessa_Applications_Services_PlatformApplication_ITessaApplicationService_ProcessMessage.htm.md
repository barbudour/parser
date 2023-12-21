# ITessaApplicationService.ProcessMessage - метод
Обрабатывает сообщение
## __Definition
 **Пространство имён:**
[Tessa.Applications.Services.PlatformApplication](N_Tessa_Applications_Services_PlatformApplication.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [OperationContractAttribute]
    [ServiceKnownTypeAttribute(typeof(ApplicationStartMessage))]
    [ServiceKnownTypeAttribute(typeof(ApplicationLinkMessage))]
    bool ProcessMessage(
    	[NotNullAttribute] ApplicationMessage message
    )
VB __Копировать
    <OperationContractAttribute>
    <ServiceKnownTypeAttribute(GetType(ApplicationStartMessage))>
    <ServiceKnownTypeAttribute(GetType(ApplicationLinkMessage))>
    Function ProcessMessage ( 
    	<NotNullAttribute> message As ApplicationMessage
    ) As Boolean
C++ __Копировать
    [OperationContractAttribute]
    [ServiceKnownTypeAttribute(typeof(ApplicationStartMessage))]
    [ServiceKnownTypeAttribute(typeof(ApplicationLinkMessage))]
    bool ProcessMessage(
    	[NotNullAttribute] ApplicationMessage^ message
    )
F# __Копировать
     [<OperationContractAttribute>]
    [<ServiceKnownTypeAttribute(typeof(ApplicationStartMessage))>]
    [<ServiceKnownTypeAttribute(typeof(ApplicationLinkMessage))>]
    abstract ProcessMessage : 
            [<NotNullAttribute>] message : ApplicationMessage -> bool 
#### Параметры
message
[ApplicationMessage](T_Tessa_Applications_Messages_ApplicationMessage.htm)
     Сообщение 
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если сообщение обработано; иначе - false
## __См. также
#### Ссылки
[ITessaApplicationService -
](T_Tessa_Applications_Services_PlatformApplication_ITessaApplicationService.htm)
[Tessa.Applications.Services.PlatformApplication - пространство
имён](N_Tessa_Applications_Services_PlatformApplication.htm)
