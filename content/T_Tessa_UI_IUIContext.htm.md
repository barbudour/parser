# IUIContext - интерфейс
Контекст операции с пользовательским интерфейсом.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public interface IUIContext : ISealable
VB __Копировать
     Public Interface IUIContext
    	Inherits ISealable
C++ __Копировать
     public interface class IUIContext : ISealable
F# __Копировать
     type IUIContext = 
        interface
            interface ISealable
        end
Implements
    [ISealable](T_Tessa_Platform_ISealable.htm)
##  __Свойства
[ActionOverridings](P_Tessa_UI_IUIContext_ActionOverridings.htm)|  Набор
переопределенных действий в текущем контексте или null, если в контексте нет
переопределенных действий.  
---|---  
[CardEditor](P_Tessa_UI_IUIContext_CardEditor.htm)|  Редактор карточки или
null, если в контексте размещена не карточка.  
[Info](P_Tessa_UI_IUIContext_Info.htm)|  Информация, связанная с контекстом и
изменяемая в расширениях. Возвращённый объект гарантированно не равен null.
Сохраняемая информация может быть несериализуемой, например, можно записать
ссылки на модели представлений или любые другие объекты.  
[InputBindings](P_Tessa_UI_IUIContext_InputBindings.htm)|  Коллекция объектов
[System.Windows.Input.InputBinding], связанных с текущим контекстом.  
[IsSealed](P_Tessa_Platform_ISealable_IsSealed.htm)| Признак того, что объект
был защищён от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
[Parent](P_Tessa_UI_IUIContext_Parent.htm)|  Родительский контекст или null,
если родительский контекст отсутствует.  
[TileContext](P_Tessa_UI_IUIContext_TileContext.htm)|  Объект, управляющий
информацией по плиткам. Возвращённое значение не равно null.  
[Tiles](P_Tessa_UI_IUIContext_Tiles.htm)|  Рабочая область с плитками или
null, если плитки не были инициализированы.  
[ViewContext](P_Tessa_UI_IUIContext_ViewContext.htm)|  Информация по
представлению или null, если в контексте размещено не представление.  
## __Методы
[IsClosed](M_Tessa_UI_IUIContext_IsClosed.htm)|  Возвращает признак того, что
контекст закрыт (например, закрыта вкладка карточки или диалог), поэтому он не
может использоваться как родительский для других создаваемых контекстов.  
---|---  
[Seal](M_Tessa_Platform_ISealable_Seal.htm)| Защищает объект от изменений.  
(Унаследован от [ISealable](T_Tessa_Platform_ISealable.htm))  
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
[InvokeDialogClosingActionAsync](M_Tessa_UI_Cards_CardUIExtensions_InvokeDialogClosingActionAsync.htm)|
Выполняет действие при закрытии окна Advanced диалога.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[InvokeDialogClosingBeforeSavingActionAsync](M_Tessa_UI_Cards_CardUIExtensions_InvokeDialogClosingBeforeSavingActionAsync.htm)|
Выполнить событие при закрытии окна Advanced диалога перед его сохранением.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[SetCardCreationInfo](M_Tessa_UI_Cards_CardUIExtensions_SetCardCreationInfo.htm)|
Устанавливает информацию по созданию карточки в контексте IUIContext.  
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
Возвращает информацию по созданию карточки в контексте IUIContext или null,
если такая информация не установлена.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
