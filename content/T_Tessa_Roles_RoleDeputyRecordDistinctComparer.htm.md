# RoleDeputyRecordDistinctComparer - класс
Сравнивает записи о заместителях на роль по свойствам
[ID](P_Tessa_Platform_CollectionRecord_ID.htm) и
[DeputyID](P_Tessa_Roles_RoleDeputyRecord_DeputyID.htm).
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class RoleDeputyRecordDistinctComparer : IEqualityComparer<RoleDeputyRecord>
VB __Копировать
     Public NotInheritable Class RoleDeputyRecordDistinctComparer
    	Implements IEqualityComparer(Of RoleDeputyRecord)
C++ __Копировать
     public ref class RoleDeputyRecordDistinctComparer sealed : IEqualityComparer<RoleDeputyRecord^>
F# __Копировать
     [<SealedAttribute>]
    type RoleDeputyRecordDistinctComparer = 
        class
            interface IEqualityComparer<RoleDeputyRecord>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ RoleDeputyRecordDistinctComparer
Implements
    [IEqualityComparer](https://learn.microsoft.com/dotnet/api/system.collections.generic.iequalitycomparer-1)<[RoleDeputyRecord](T_Tessa_Roles_RoleDeputyRecord.htm)>
##  __Конструкторы
[RoleDeputyRecordDistinctComparer](M_Tessa_Roles_RoleDeputyRecordDistinctComparer__ctor.htm)|
Инициализирует новый экземпляр класса RoleDeputyRecordDistinctComparer  
---|---  
##  __Свойства
[Instance](P_Tessa_Roles_RoleDeputyRecordDistinctComparer_Instance.htm)|
Экземпляр объекта.  
---|---  
## __Методы
[Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
[Equals(RoleDeputyRecord,
RoleDeputyRecord)](M_Tessa_Roles_RoleDeputyRecordDistinctComparer_Equals.htm)|
Сравнивает записи о заместителях на роль по свойствам
[ID](P_Tessa_Platform_CollectionRecord_ID.htm) и
[DeputyID](P_Tessa_Roles_RoleDeputyRecord_DeputyID.htm).  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode(RoleDeputyRecord)](M_Tessa_Roles_RoleDeputyRecordDistinctComparer_GetHashCode.htm)|
Возвращает хеш-код записи.  
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
[Tessa.Roles - пространство имён](N_Tessa_Roles.htm)
