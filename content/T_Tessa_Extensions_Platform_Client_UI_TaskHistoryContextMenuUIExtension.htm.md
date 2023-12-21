# TaskHistoryContextMenuUIExtension - класс
Контекстное меню по умолчанию для всех записей в истории заданий.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Platform.Client.UI](N_Tessa_Extensions_Platform_Client_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class TaskHistoryContextMenuUIExtension : CardUIExtension
VB __Копировать
     Public NotInheritable Class TaskHistoryContextMenuUIExtension
    	Inherits CardUIExtension
C++ __Копировать
     public ref class TaskHistoryContextMenuUIExtension sealed : public CardUIExtension
F# __Копировать
     [<SealedAttribute>]
    type TaskHistoryContextMenuUIExtension = 
        class
            inherit CardUIExtension
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm) __ TaskHistoryContextMenuUIExtension
##  __Конструкторы
[TaskHistoryContextMenuUIExtension](M_Tessa_Extensions_Platform_Client_UI_TaskHistoryContextMenuUIExtension__ctor.htm)|
Инициализирует новый экземпляр класса TaskHistoryContextMenuUIExtension  
---|---  
##  __Методы
[ContextInitialized](M_Tessa_UI_Cards_CardUIExtension_ContextInitialized.htm)|
Выполняется при инициализации контекста [Tessa.UI.IUIContext], который
связывается с плитками IUIContext.Tiles при открытии редактора во вкладке, а
также при каждом переоткрытии карточки в этом контексте. Метод похож на
Initialized, но выполняется только для физически существующих во вкладках
карточек, которые связаны с плитками, доступными посредством
context.UIContext.Tiles. Расширение гарантированно будет вызвано при открытии
вкладки с карточкой штатными средствами, но может не быть вызвано, например,
при просмотре удалённой карточки или при редактировании карточки внутри
шаблона. Если при выполнении расширения возникли ошибки, то вкладка визуально
не будет открыта, и будут выполнены расширения на закрытие вкладки. Метод
может выполняться асинхронно относительно потока UI. Не вызывайте методы,
выполняемые в потоке UI асинхронно, такие как
DispatcherHelper.InvokeInUIAsync.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
---|---  
[ContextInitializedFinally](M_Tessa_UI_Cards_CardUIExtension_ContextInitializedFinally.htm)|
Выполняется при инициализации контекста [Tessa.UI.IUIContext] после выполнения
методов [ICardUIExtension.ContextInitialized]. Необработанные исключения не
прерывают выполнение цепочки расширений. Метод может выполняться асинхронно
относительно потока UI. Не вызывайте методы, выполняемые в потоке UI
асинхронно, такие как DispatcherHelper.InvokeInUIAsync.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Finalized](M_Tessa_UI_Cards_CardUIExtension_Finalized.htm)|  Выполняется при
финализации модели представления карточки. Происходит при окончательном
закрытии редактора или при загрузке новой карточки в тот же редактор.
Выполнение производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[Finalizing](M_Tessa_UI_Cards_CardUIExtension_Finalizing.htm)|  Выполняется
при финализации модели представления карточки. Происходит при попытке закрыть
редактор или при загрузке новой карточки в тот же редактор. Выполнение
производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Initialized](M_Tessa_Extensions_Platform_Client_UI_TaskHistoryContextMenuUIExtension_Initialized.htm)|  
(Переопределяет
[CardUIExtension.Initialized(ICardUIExtensionContext)](M_Tessa_UI_Cards_CardUIExtension_Initialized.htm))  
[InitializedFinally](M_Tessa_UI_Cards_CardUIExtension_InitializedFinally.htm)|
Выполняется при инициализации модели представления карточки после выполнения
методов [ICardUIExtension.Initialized]. Необработанные исключения не прерывают
выполнение цепочки расширений. При этом уже созданы и заполнены все модели
представления. Выполнение производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[Initializing](M_Tessa_UI_Cards_CardUIExtension_Initializing.htm)|
Выполняется перед инициализацией модели представления карточки. При этом уже
доступна карточка и некоторые действия с моделью, но ещё не созданы и не
заполнены все модели представления. Выполнение производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Reopened](M_Tessa_UI_Cards_CardUIExtension_Reopened.htm)|  Выполняется после
повторного открытия карточки, которое вызвано любым способом из редактора
карточек [Tessa.UI.Cards.ICardEditorModel], в том числе при открытии после
сохранения. В метод передаётся пакет загруженной карточки. Метод может
изменить объект [Tessa.UI.Cards.ICardModel] до того, как он будет создан
стандартным образом, чтобы установить специальные флаги модели представления
или создать модель представления для другой карточки. В свойстве
[Tessa.UI.Cards.ICardUIExtensionContext.Model] объект получает предыдущую
версию модели представления карточки, которая будет отброшена после успешного
открытия. Выполнение производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[Reopening](M_Tessa_UI_Cards_CardUIExtension_Reopening.htm)|  Выполняется
перед повторным открытием карточки, которое вызвано любым способом из
редактора карточек [Tessa.UI.Cards.ICardEditorModel], в том числе при открытии
после сохранения. Метод может изменить запрос на загрузку карточки перед его
выполнением. В свойстве [Tessa.UI.Cards.ICardUIExtensionContext.Model] объект
получает предыдущую версию модели представления карточки, которая будет
отброшена после успешного открытия. Выполнение производится в потоке UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[Saving](M_Tessa_UI_Cards_CardUIExtension_Saving.htm)|  Выполняется перед
сохранением карточки, которое вызвано любым способом из редактора карточек
[Tessa.UI.Cards.ICardEditorModel], в том числе при завершении задания или
закрытии вкладки с сохранением. В метод передаётся пакет карточки, изменённый
перед сохранением, а также исходный объект [Tessa.UI.Cards.ICardModel]. Метод
позволяет выполнить любые подготовительные действия, в т.ч. затрагивающие
изменение файлов карточки, вследствие чего будет применено обычное или
потоковое сохранение карточки. Выполнение производится в том же потоке, в
которой вызывалось сохранение карточки. Обычно это поток, асинхронный по
отношению к UI.  
(Унаследован от [CardUIExtension](T_Tessa_UI_Cards_CardUIExtension.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
##  __См. также
#### Ссылки
[Tessa.Extensions.Platform.Client.UI - пространство
имён](N_Tessa_Extensions_Platform_Client_UI.htm)
