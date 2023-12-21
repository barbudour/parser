# SharedEventInstanceList<TEventArgs> \- класс
Список, содержащий информацию о произошедшем событии, синхронизация которого
выполняется из различных процессов.
## __Definition
 **Пространство имён:** [Tessa.Platform.IPC](N_Tessa_Platform_IPC.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class SharedEventInstanceList<TEventArgs> : SharedInstanceList
    where TEventArgs : class, new(), ISharedEventArgs
VB __Копировать
     Public Class SharedEventInstanceList(Of TEventArgs As {Class, New, ISharedEventArgs})
    	Inherits SharedInstanceList
C++ __Копировать
    generic<typename TEventArgs>
    where TEventArgs : ref class, gcnew(), ISharedEventArgs
    public ref class SharedEventInstanceList : public SharedInstanceList
F# __Копировать
     type SharedEventInstanceList<'TEventArgs when 'TEventArgs : not struct, new() and ISharedEventArgs> = 
        class
            inherit SharedInstanceList
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm) __ SharedEventInstanceList<TEventArgs>
#### Параметры типа
TEventArgs
     Ссылочный тип аргументов события, содержащий конструктор по умолчанию. 
## __Конструкторы
[SharedEventInstanceList<TEventArgs>()](M_Tessa_Platform_IPC_SharedEventInstanceList_1__ctor.htm)|
Создаёт экземпляр класса с параметрами по умолчанию.  
---|---  
[SharedEventInstanceList<TEventArgs>(SharedEventInstanceList<TEventArgs>)](M_Tessa_Platform_IPC_SharedEventInstanceList_1__ctor_1.htm)|
Создаёт экземпляр класса, содержащий копию заданной информации о событии.  
[SharedEventInstanceList<TEventArgs>(SharedInstanceList, Guid,
TEventArgs)](M_Tessa_Platform_IPC_SharedEventInstanceList_1__ctor_2.htm)|
Создаёт экземпляр класса, содержащий копию заданной информации о подписчиках
на событие, уникальный идентификатор произошедшего события и аргументы
события.  
## __Свойства
[EventArgs](P_Tessa_Platform_IPC_SharedEventInstanceList_1_EventArgs.htm)|
Аргументы события.  
---|---  
[EventID](P_Tessa_Platform_IPC_SharedEventInstanceList_1_EventID.htm)|
Уникальный идентификатор события.  
[IsEmpty](P_Tessa_Platform_IPC_SharedInstanceList_IsEmpty.htm)|  Признак того,
что список не содержит значений.  
(Унаследован от
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm))  
##  __Методы
[AddInstance](M_Tessa_Platform_IPC_SharedInstanceList_AddInstance.htm)|
Добавляет в список информацию об экземляре объекта, расположенного в текущем
процессе, синхронизация которого выполняется.  
(Унаследован от
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm))  
---|---  
[Deserialize](M_Tessa_Platform_IPC_SharedEventInstanceList_1_Deserialize.htm)|
Десериализует объект из бинарной формы.  
(Переопределяет
[SharedInstanceList.Deserialize(BinaryReader)](M_Tessa_Platform_IPC_SharedInstanceList_Deserialize.htm))  
[Dispose](M_Tessa_Platform_IPC_SharedInstanceList_Dispose.htm)|  
(Унаследован от
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm))  
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
(Унаследован от
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm))  
[RemoveInstance](M_Tessa_Platform_IPC_SharedInstanceList_RemoveInstance.htm)|
Удаляет из списка информацию о текущем процессе.  
(Унаследован от
[SharedInstanceList](T_Tessa_Platform_IPC_SharedInstanceList.htm))  
[Serialize](M_Tessa_Platform_IPC_SharedEventInstanceList_1_Serialize.htm)|
Сериализует объект в бинарной форме.  
(Переопределяет
[SharedInstanceList.Serialize(BinaryWriter)](M_Tessa_Platform_IPC_SharedInstanceList_Serialize.htm))  
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
