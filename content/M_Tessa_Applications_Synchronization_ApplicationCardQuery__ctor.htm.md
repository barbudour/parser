# ApplicationCardQuery - конструктор
Initializes a new instance of the
[ApplicationCardQuery](T_Tessa_Applications_Synchronization_ApplicationCardQuery.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationCardQuery(
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] IAvailableApplicationsQuery query,
    	Func<ICardGetComponent> cardGetComponentFunc,
    	[NotNullAttribute] Func<ISession> sessionFunc,
    	[NotNullAttribute] Func<ICardMetadata> cardMetadataFunc
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> query As IAvailableApplicationsQuery,
    	cardGetComponentFunc As Func(Of ICardGetComponent),
    	<NotNullAttribute> sessionFunc As Func(Of ISession),
    	<NotNullAttribute> cardMetadataFunc As Func(Of ICardMetadata)
    )
C++ __Копировать
     public:
    ApplicationCardQuery(
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] IAvailableApplicationsQuery^ query, 
    	Func<ICardGetComponent^>^ cardGetComponentFunc, 
    	[NotNullAttribute] Func<ISession^>^ sessionFunc, 
    	[NotNullAttribute] Func<ICardMetadata^>^ cardMetadataFunc
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] query : IAvailableApplicationsQuery * 
            cardGetComponentFunc : Func<ICardGetComponent> * 
            [<NotNullAttribute>] sessionFunc : Func<ISession> * 
            [<NotNullAttribute>] cardMetadataFunc : Func<ICardMetadata> -> ApplicationCardQuery
#### Параметры
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Контроллер открытых сессий 
query
[IAvailableApplicationsQuery](T_Tessa_Applications_Synchronization_IAvailableApplicationsQuery.htm)
     Запрос на получение информации о доступных приложениях 
cardGetComponentFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardGetComponent](T_Tessa_Cards_ComponentModel_ICardGetComponent.htm)>
     The card Get Component Func. 
sessionFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ISession](T_Tessa_Platform_Runtime_ISession.htm)>
     The session Func. 
cardMetadataFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)>
     The card Metadata Func. 
## __См. также
#### Ссылки
[ApplicationCardQuery -
](T_Tessa_Applications_Synchronization_ApplicationCardQuery.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
