# Command - класс
Команда
[ICommand](https://learn.microsoft.com/dotnet/api/system.windows.input.icommand),
используемая в пользовательском интерфейсе для выполнения действий.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public abstract class Command : ICommand
VB __Копировать
     Public MustInherit Class Command
    	Implements ICommand
C++ __Копировать
     public ref class Command abstract : ICommand
F# __Копировать
     [<AbstractClassAttribute>]
    type Command = 
        class
            interface ICommand
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ Command
Derived
[Tessa.Extensions.Platform.Client.Application.OpenWorkplaceCommand](T_Tessa_Extensions_Platform_Client_Application_OpenWorkplaceCommand.htm)
[Tessa.UI.AggregateCommand](T_Tessa_UI_AggregateCommand.htm)
[Tessa.UI.AppManager.CatalogService.CreateDesktopShortcutCommand](T_Tessa_UI_AppManager_CatalogService_CreateDesktopShortcutCommand.htm)
[Tessa.UI.AppManager.CatalogService.LaunchNewInstanceCommand](T_Tessa_UI_AppManager_CatalogService_LaunchNewInstanceCommand.htm)
[Tessa.UI.AppManager.CatalogService.SetDefaultCatalogCommand](T_Tessa_UI_AppManager_CatalogService_SetDefaultCatalogCommand.htm)
[Tessa.UI.DelegateCommand](T_Tessa_UI_DelegateCommand.htm)
[Tessa.UI.DelegateCommand<T>](T_Tessa_UI_DelegateCommand_1.htm)
[Tessa.UI.HashEditor.Hash.DeleteCollectionNodeCommand](T_Tessa_UI_HashEditor_Hash_DeleteCollectionNodeCommand.htm)
[Tessa.UI.HashEditor.Hash.DeleteDictionaryKeyCommand](T_Tessa_UI_HashEditor_Hash_DeleteDictionaryKeyCommand.htm)
Подробнее __Less __
Implements
    [ICommand](https://learn.microsoft.com/dotnet/api/system.windows.input.icommand)
##  __Конструкторы
[Command](M_Tessa_UI_Command__ctor.htm)| Инициализирует новый экземпляр класса
Command  
---|---  
##  __Методы
[CanExecute](M_Tessa_UI_Command_CanExecute.htm)| Определяет признак
доступности команды.  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Execute](M_Tessa_UI_Command_Execute.htm)| Выполняет команду с заданным
параметром.  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[RaiseCanExecuteChanged](M_Tessa_UI_Command_RaiseCanExecuteChanged.htm)|
Уведомляет диспетчер событий о том, что метод
[CanExecute(Object)](M_Tessa_UI_Command_CanExecute.htm) команды будет выдавать
другой результат.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CanExecuteChanged](E_Tessa_UI_Command_CanExecuteChanged.htm)|  Событие,
определяющее момент, когда необходимо проверить доступность команды.  
---|---  
## __Методы расширения
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
