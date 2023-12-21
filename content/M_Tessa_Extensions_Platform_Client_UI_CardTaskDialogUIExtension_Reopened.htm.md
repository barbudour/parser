# CardTaskDialogUIExtension.Reopened - метод
Выполняется после повторного открытия карточки, которое вызвано любым способом
из редактора карточек [Tessa.UI.Cards.ICardEditorModel], в том числе при
открытии после сохранения. В метод передаётся пакет загруженной карточки.
Метод может изменить объект [Tessa.UI.Cards.ICardModel] до того, как он будет
создан стандартным образом, чтобы установить специальные флаги модели
представления или создать модель представления для другой карточки. В свойстве
[Tessa.UI.Cards.ICardUIExtensionContext.Model] объект получает предыдущую
версию модели представления карточки, которая будет отброшена после успешного
открытия. Выполнение производится в потоке UI.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task Reopened(
    	ICardUIExtensionContext context
    )
VB __Копировать
     Public Overrides Function Reopened ( 
    	context As ICardUIExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ Reopened(
    	ICardUIExtensionContext^ context
    ) override
F# __Копировать
     abstract Reopened : 
            context : ICardUIExtensionContext -> Task 
    override Reopened : 
            context : ICardUIExtensionContext -> Task 
#### Параметры
context
[ICardUIExtensionContext](T_Tessa_UI_Cards_ICardUIExtensionContext.htm)
    Контекст модели представления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardUIExtension.Reopened(ICardUIExtensionContext)](M_Tessa_UI_Cards_ICardUIExtension_Reopened.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardTaskDialogUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
