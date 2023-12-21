# CardTaskDialogUIExtension.Saving - метод
Выполняется перед сохранением карточки, которое вызвано любым способом из
редактора карточек [Tessa.UI.Cards.ICardEditorModel], в том числе при
завершении задания или закрытии вкладки с сохранением. В метод передаётся
пакет карточки, изменённый перед сохранением, а также исходный объект
[Tessa.UI.Cards.ICardModel]. Метод позволяет выполнить любые подготовительные
действия, в т.ч. затрагивающие изменение файлов карточки, вследствие чего
будет применено обычное или потоковое сохранение карточки. Выполнение
производится в том же потоке, в которой вызывалось сохранение карточки. Обычно
это поток, асинхронный по отношению к UI.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public override Task Saving(
    	ICardUIExtensionContext context
    )
VB __Копировать
     Public Overrides Function Saving ( 
    	context As ICardUIExtensionContext
    ) As Task
C++ __Копировать
     public:
    virtual Task^ Saving(
    	ICardUIExtensionContext^ context
    ) override
F# __Копировать
     abstract Saving : 
            context : ICardUIExtensionContext -> Task 
    override Saving : 
            context : ICardUIExtensionContext -> Task 
#### Параметры
context
[ICardUIExtensionContext](T_Tessa_UI_Cards_ICardUIExtensionContext.htm)
    Контекст модели представления карточки.
#### Возвращаемое значение
[Task](https://learn.microsoft.com/dotnet/api/system.threading.tasks.task)  
Асинхронная задача.
#### Реализации
[ICardUIExtension.Saving(ICardUIExtensionContext)](M_Tessa_UI_Cards_ICardUIExtension_Saving.htm)  
##  __Заметки
По умолчанию метод не выполняет действий.
##  __См. также
#### Ссылки
[CardTaskDialogUIExtension -
](T_Tessa_Extensions_Platform_Client_UI_CardTaskDialogUIExtension.htm)
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
