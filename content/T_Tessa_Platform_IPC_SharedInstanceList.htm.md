# SharedInstanceList - класс
Список, содержащий информацию об экземплярах, синхронизация которых
выполняется из различных процессов.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SharedInstanceList : IBinarySerializable, 
    	IDisposable
VB __Копировать
     Public Class SharedInstanceList
    	Implements IBinarySerializable, IDisposable
C++ __Копировать
     public ref class SharedInstanceList : IBinarySerializable, 
    	IDisposable
F# __Копировать
     type SharedInstanceList = 
        class
            interface IBinarySerializable
            interface IDisposable
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SharedInstanceList
Derived
[Tessa.Platform.IPC.SharedEventInstanceList<TEventArgs>](T_Tessa_Platform_IPC_SharedEventInstanceList_1.htm)
Implements
    [IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable), [IBinarySerializable](T_Tessa_Platform_IBinarySerializable.htm)
##  __Конструкторы
[SharedInstanceList()](M_Tessa_Platform_IPC_SharedInstanceList__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SharedInstanceList(SharedInstanceList)](M_Tessa_Platform_IPC_SharedInstanceList__ctor_1.htm)|
Создаёт экземпляр класса, содержащий копию заданного списка.  
## __Свойства
[IsEmpty](P_Tessa_Platform_IPC_SharedInstanceList_IsEmpty.htm)|  Признак того,
что список не содержит значений.  
---|---  
## __Методы
[AddInstance](M_Tessa_Platform_IPC_SharedInstanceList_AddInstance.htm)|
Добавляет в список информацию об экземляре объекта, расположенного в текущем
процессе, синхронизация которого выполняется.  
---|---  
[Deserialize](M_Tessa_Platform_IPC_SharedInstanceList_Deserialize.htm)|
Десериализует объект из бинарной формы.  
[Dispose](M_Tessa_Platform_IPC_SharedInstanceList_Dispose.htm)| Освобождает
все ресурсы, используемые объектом SharedInstanceList  
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
[RemoveDeadProcesses](M_Tessa_Platform_IPC_SharedInstanceList_RemoveDeadProcesses.htm)|
Удаляет информацию о всех процессах, которые уже не существуют на момент
проверки.  
[RemoveInstance](M_Tessa_Platform_IPC_SharedInstanceList_RemoveInstance.htm)|
Удаляет из списка информацию о текущем процессе.  
[Serialize](M_Tessa_Platform_IPC_SharedInstanceList_Serialize.htm)|
Сериализует объект в бинарной форме.  
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
[Tessa.Platform.IPC - пространство имён](N_Tessa_Platform_IPC.htm)
