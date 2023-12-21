# CardTaskDialogUIExtension - конструктор
Инициализирует новый экземпляр класса.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public CardTaskDialogUIExtension(
    	IAdvancedCardDialogManager advancedCardDialogManager,
    	ICardMetadata cardMetadata,
    	Func<ICardEditorModel> createCardEditorFunc,
    	ISession session,
    	ICardRepository cardRepository
    )
VB __Копировать
     Public Sub New ( 
    	advancedCardDialogManager As IAdvancedCardDialogManager,
    	cardMetadata As ICardMetadata,
    	createCardEditorFunc As Func(Of ICardEditorModel),
    	session As ISession,
    	cardRepository As ICardRepository
    )
C++ __Копировать
     public:
    CardTaskDialogUIExtension(
    	IAdvancedCardDialogManager^ advancedCardDialogManager, 
    	ICardMetadata^ cardMetadata, 
    	Func<ICardEditorModel^>^ createCardEditorFunc, 
    	ISession^ session, 
    	ICardRepository^ cardRepository
    )
F# __Копировать
     new : 
            advancedCardDialogManager : IAdvancedCardDialogManager * 
            cardMetadata : ICardMetadata * 
            createCardEditorFunc : Func<ICardEditorModel> * 
            session : ISession * 
            cardRepository : ICardRepository -> CardTaskDialogUIExtension
#### Параметры
advancedCardDialogManager
[IAdvancedCardDialogManager](T_Tessa_UI_Cards_IAdvancedCardDialogManager.htm)
Объект, предоставляющий методы для открытий карточки в модальном диалоге.
cardMetadata [ICardMetadata](T_Tessa_Cards_ICardMetadata.htm)
Содержит метаинформацию, необходимую для использования типов карточек
совместно с пакетом карточек.
createCardEditorFunc
[Func](https://learn.microsoft.com/dotnet/api/system.func-1)<[ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm)>
    Функция для создания [ICardEditorModel](T_Tessa_UI_Cards_ICardEditorModel.htm).
session [ISession](T_Tessa_Platform_Runtime_ISession.htm)
Сессия пользователя.
cardRepository [ICardRepository](T_Tessa_Cards_ICardRepository.htm)
Репозиторий для управления карточками.
## __См. также
#### Ссылки
[CardTaskDialogUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
