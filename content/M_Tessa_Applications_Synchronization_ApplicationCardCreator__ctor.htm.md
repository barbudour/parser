# ApplicationCardCreator - конструктор
Initializes a new instance of the
[ApplicationCardCreator](T_Tessa_Applications_Synchronization_ApplicationCardCreator.htm)
class. Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.
## __Definition
 **Пространство имён:**
[Tessa.Applications.Synchronization](N_Tessa_Applications_Synchronization.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public ApplicationCardCreator(
    	[NotNullAttribute] ISessionController sessionController,
    	[NotNullAttribute] ICardRepository cardRepository
    )
VB __Копировать
     Public Sub New ( 
    	<NotNullAttribute> sessionController As ISessionController,
    	<NotNullAttribute> cardRepository As ICardRepository
    )
C++ __Копировать
     public:
    ApplicationCardCreator(
    	[NotNullAttribute] ISessionController^ sessionController, 
    	[NotNullAttribute] ICardRepository^ cardRepository
    )
F# __Копировать
     new : 
            [<NotNullAttribute>] sessionController : ISessionController * 
            [<NotNullAttribute>] cardRepository : ICardRepository -> ApplicationCardCreator
#### Параметры
sessionController
[ISessionController](T_Tessa_Applications_ISessionController.htm)
     Контроллер управления состоянием сессии 
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
     Репозиторий карточек 
## __См. также
#### Ссылки
[ApplicationCardCreator -
](T_Tessa_Applications_Synchronization_ApplicationCardCreator.htm)
[Tessa.Applications.Synchronization - пространство
имён](N_Tessa_Applications_Synchronization.htm)
