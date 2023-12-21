# UIContext - класс
Контекст операции с пользовательским интерфейсом.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class UIContext : IUIContext, 
    	ISealable
VB __Копировать
     Public NotInheritable Class UIContext
    	Implements IUIContext, ISealable
C++ __Копировать
     public ref class UIContext sealed : IUIContext, 
    	ISealable
F# __Копировать
     [<SealedAttribute>]
    type UIContext = 
        class
            interface IUIContext
            interface ISealable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ UIContext
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm), [IUIContext](T_Tessa_UI_IUIContext.htm)
##  __Конструкторы
[UIContext(Func<IViewContext>, IUIContextActionOverridings, IUIContext,
Boolean)](M_Tessa_UI_UIContext__ctor.htm)|  Инициализирует новый экземпляр
класса UIContext.  
---|---  
[UIContext(ICardEditorModel, IUIContextActionOverridings, IUIContext,
Boolean)](M_Tessa_UI_UIContext__ctor_2.htm)|  Создаёт экземпляр класса с
указанием параметров контекста.  
[UIContext(IViewContext, IUIContextActionOverridings, IUIContext,
Boolean)](M_Tessa_UI_UIContext__ctor_4.htm)|  Инициализирует новый экземпляр
класса UIContext.  
[UIContext(ICardEditorModel, Func<IViewContext>, IUIContextActionOverridings,
IUIContext, Boolean)](M_Tessa_UI_UIContext__ctor_1.htm)|  Инициализирует новый
экземпляр класса UIContext.  
[UIContext(ICardEditorModel, IViewContext, IUIContextActionOverridings,
IUIContext, Boolean)](M_Tessa_UI_UIContext__ctor_3.htm)|  Инициализирует новый
экземпляр класса UIContext.  
## __Свойства
[ActionOverridings](P_Tessa_UI_UIContext_ActionOverridings.htm)|  Набор
переопределенных действий в текущем контексте или null, если в контексте нет
переопределенных действий.  
---|---  
[CardEditor](P_Tessa_UI_UIContext_CardEditor.htm)|  Редактор карточки или
null, если в контексте размещена не карточка.  
[Current](P_Tessa_UI_UIContext_Current.htm)|  Текущий контекст
[IUIContext](T_Tessa_UI_IUIContext.htm).  
[HasCurrent](P_Tessa_UI_UIContext_HasCurrent.htm)|  Признак того, что текущий
код выполняется внутри операции с контекстом
[IUIContext](T_Tessa_UI_IUIContext.htm), а свойство
[Current](P_Tessa_UI_UIContext_Current.htm) ссылается на действительный
контекст.  
[Info](P_Tessa_UI_UIContext_Info.htm)|  Информация, связанная с контекстом и
изменяемая в расширениях. Возвращённый объект гарантированно не равен null.
Сохраняемая информация может быть несериализуемой, например, можно записать
ссылки на модели представлений или любые другие объекты.  
[InputBindings](P_Tessa_UI_UIContext_InputBindings.htm)|  Коллекция объектов
[System.Windows.Input.InputBinding], связанных с текущим контекстом.  
[IsSealed](P_Tessa_UI_UIContext_IsSealed.htm)| Признак того, что объект был
защищён от изменений.  
[Parent](P_Tessa_UI_UIContext_Parent.htm)|  Родительский контекст или null,
если родительский контекст отсутствует.  
[TileContext](P_Tessa_UI_UIContext_TileContext.htm)|  Объект, управляющий
информацией по плиткам. Возвращённое значение не равно null.  
[Tiles](P_Tessa_UI_UIContext_Tiles.htm)|  Рабочая область с плитками или null,
если плитки не были инициализированы.  
[Unknown](P_Tessa_UI_UIContext_Unknown.htm)|  Неизвестный контекст
[IUIContext](T_Tessa_UI_IUIContext.htm).  
[ViewContext](P_Tessa_UI_UIContext_ViewContext.htm)|  Информация по
представлению или null, если в контексте размещено не представление.  
## __Методы
[Create](M_Tessa_UI_UIContext_Create.htm)|  Создаёт область операции, в
которой заданный контекст будет являться текущим.  
---|---  
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
[IsClosed](M_Tessa_UI_UIContext_IsClosed.htm)|  Возвращает признак того, что
контекст закрыт (например, закрыта вкладка карточки или диалог), поэтому он не
может использоваться как родительский для других создаваемых контекстов.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Seal](M_Tessa_UI_UIContext_Seal.htm)| Защищает объект от изменений.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __Методы расширения
[AddInputBinding](M_Tessa_UI_UIExtensions_AddInputBinding.htm)|  Добавляет
привязку на заданный жест для выполнения команды плитки, если выполнение такой
команды разрешено.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
---|---  
[AddKeyBinding](M_Tessa_UI_UIExtensions_AddKeyBinding.htm)|  Добавляет
привязку на горячую клавишу для выполнения команды плитки, если выполнение
такой команды разрешено.  
(Определяется [UIExtensions](T_Tessa_UI_UIExtensions.htm))  
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InternalMarkerCanvas](M_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor_InternalMarkerCanvas.htm)|
Возвращает маркер аннотации  
(Определяется
[AnnotationInternalsAccessor](T_Tessa_UI_Views_Charting_Annotations_AnnotationInternalsAccessor.htm))  
[Invoke](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Invoke.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[InvokeDialogClosingActionAsync](M_Tessa_UI_Cards_CardUIExtensions_InvokeDialogClosingActionAsync.htm)|
Выполняет действие при закрытии окна Advanced диалога.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[InvokeDialogClosingBeforeSavingActionAsync](M_Tessa_UI_Cards_CardUIExtensions_InvokeDialogClosingBeforeSavingActionAsync.htm)|
Выполнить событие при закрытии окна Advanced диалога перед его сохранением.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[Set](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Set.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
[SetCardCreationInfo](M_Tessa_UI_Cards_CardUIExtensions_SetCardCreationInfo.htm)|
Устанавливает информацию по созданию карточки в контексте
[IUIContext](T_Tessa_UI_IUIContext.htm).  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[SetDialogClosingAction](M_Tessa_UI_Cards_CardUIExtensions_SetDialogClosingAction.htm)|
Устанавливает действие, выполняемое при закрытии окна Advanced диалога.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[SetDialogClosingBeforeSavingAction](M_Tessa_UI_Cards_CardUIExtensions_SetDialogClosingBeforeSavingAction.htm)|
Устанавливает действие, выполняемое при закрытии окна Advanced диалога перед
его сохранением. Возникает, когда есть изменения в карточке, пользователю
отобразился диалог с сохранением изменений и пользователь нажал сохранить.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[TryGetCardCreationInfo](M_Tessa_UI_Cards_CardUIExtensions_TryGetCardCreationInfo.htm)|
Возвращает информацию по созданию карточки в контексте
[IUIContext](T_Tessa_UI_IUIContext.htm) или null, если такая информация не
установлена.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
