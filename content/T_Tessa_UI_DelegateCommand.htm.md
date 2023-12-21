# DelegateCommand - класс
Команда
[ICommand](https://learn.microsoft.com/dotnet/api/system.windows.input.icommand),
используемая в пользовательском интерфейсе для выполнения действий, задаваемых
делегатами.
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DelegateCommand : Command
VB __Копировать
     Public NotInheritable Class DelegateCommand
    	Inherits Command
C++ __Копировать
     public ref class DelegateCommand sealed : public Command
F# __Копировать
     [<SealedAttribute>]
    type DelegateCommand = 
        class
            inherit Command
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[Command](T_Tessa_UI_Command.htm) __ DelegateCommand
##  __Конструкторы
[DelegateCommand](M_Tessa_UI_DelegateCommand__ctor.htm)|  Создаёт экземпляр
класса с указанием делегатов, определяющих поведение команды.  
---|---  
## __Методы
[CanExecute](M_Tessa_UI_DelegateCommand_CanExecute.htm)| Определяет признак
доступности команды.  
(Переопределяет
[Command.CanExecute(Object)](M_Tessa_UI_Command_CanExecute.htm))  
---|---  
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[Execute](M_Tessa_UI_DelegateCommand_Execute.htm)| Выполняет команду с
заданным параметром.  
(Переопределяет [Command.Execute(Object)](M_Tessa_UI_Command_Execute.htm))  
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
(Унаследован от [Command](T_Tessa_UI_Command.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
##  __События
[CanExecuteChanged](E_Tessa_UI_Command_CanExecuteChanged.htm)|  Событие,
определяющее момент, когда необходимо проверить доступность команды.  
(Унаследован от [Command](T_Tessa_UI_Command.htm))  
---|---  
##  __Поля
[Empty](F_Tessa_UI_DelegateCommand_Empty.htm)|  Экземпляр команды
DelegateCommand, не выполняющей действий и всегда являющейся доступной.  
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
