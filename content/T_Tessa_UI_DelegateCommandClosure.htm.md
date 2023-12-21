# DelegateCommandClosure - класс
Замыкание, позволяющее создавать команды, сопоставленные с актуальными
значениями делегатов, которые задаются как свойства
[Execute](P_Tessa_UI_DelegateCommandClosure_Execute.htm) и
[CanExecute](P_Tessa_UI_DelegateCommandClosure_CanExecute.htm).
## __Definition
 **Пространство имён:** [Tessa.UI](N_Tessa_UI.htm)  
 **Сборка:** Tessa.UI (в Tessa.UI.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class DelegateCommandClosure : IMutableCommand
VB __Копировать
     Public NotInheritable Class DelegateCommandClosure
    	Implements IMutableCommand
C++ __Копировать
     public ref class DelegateCommandClosure sealed : IMutableCommand
F# __Копировать
     [<SealedAttribute>]
    type DelegateCommandClosure = 
        class
            interface IMutableCommand
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ DelegateCommandClosure
Implements
    [IMutableCommand](T_Tessa_UI_IMutableCommand.htm)
##  __Конструкторы
[DelegateCommandClosure](M_Tessa_UI_DelegateCommandClosure__ctor.htm)|
Инициализирует новый экземпляр класса DelegateCommandClosure  
---|---  
##  __Свойства
[CanExecute](P_Tessa_UI_DelegateCommandClosure_CanExecute.htm)|  Делегат,
определяющий доступность выполнения команд, которые были созданы для этого
объекта. По умолчанию делегат всегда возвращает true. Если задать значение
null, то также возвращается true. Изменение делегата отражается как на уже
созданный командах, так и на ещё не созданных.  
---|---  
[Execute](P_Tessa_UI_DelegateCommandClosure_Execute.htm)|  Делегат,
определяющий действие, выполняемое командами, которые были созданы для этого
объекта. По умолчанию делегат не выполняет никаких действий. Если задать
значение null, то действий также не выполняется. Изменение делегата отражается
как на уже созданный командах, так и на ещё не созданных.  
## __Методы
[CreateCommand](M_Tessa_UI_DelegateCommandClosure_CreateCommand.htm)|  Создаёт
и возвращает команду, которая сопоставлена с актуальными делегатами
[Execute](P_Tessa_UI_IMutableCommand_Execute.htm) и
[CanExecute](P_Tessa_UI_IMutableCommand_CanExecute.htm).  
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
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
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
[Tessa.UI - пространство имён](N_Tessa_UI.htm)
