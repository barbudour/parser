# RoleDeputyRecord - класс
Запись о замещении на роль.
## __Definition
 **Пространство имён:** [Tessa.Roles](N_Tessa_Roles.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [DataContractAttribute]
    [TableAttribute("RoleDeputies", IsColumnAttributeRequired = false)]
    public sealed class RoleDeputyRecord : CollectionRecord, 
    	IRoleUser
VB __Копировать
    <DataContractAttribute>
    <TableAttribute("RoleDeputies", IsColumnAttributeRequired := false)>
    Public NotInheritable Class RoleDeputyRecord
    	Inherits CollectionRecord
    	Implements IRoleUser
C++ __Копировать
    [DataContractAttribute]
    [TableAttribute(L"RoleDeputies", IsColumnAttributeRequired = false)]
    public ref class RoleDeputyRecord sealed : public CollectionRecord, 
    	IRoleUser
F# __Копировать
     [<SealedAttribute>]
    [<DataContractAttribute>]
    [<TableAttribute("RoleDeputies", IsColumnAttributeRequired = false)>]
    type RoleDeputyRecord = 
        class
            inherit CollectionRecord
            interface IRoleUser
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CollectionRecord](T_Tessa_Platform_CollectionRecord.htm) __ RoleDeputyRecord
Implements
    [IRoleUser](T_Tessa_Roles_IRoleUser.htm)
##  __Конструкторы
[RoleDeputyRecord](M_Tessa_Roles_RoleDeputyRecord__ctor.htm)| Создаёт
экземпляр класса с параметрами по умолчанию.  
---|---  
##  __Свойства
[Deputized](P_Tessa_Roles_RoleDeputyRecord_Deputized.htm)|  Роль пользователя,
замещение которого производится, или null, если производится не замещение для
конкретного пользователя, а временное включение в роль.  
---|---  
[DeputizedID](P_Tessa_Roles_RoleDeputyRecord_DeputizedID.htm)|  Идентификатор
персональной роли пользователя, замещение которого производится, или null,
если производится не замещение для конкретного пользователя, а временное
включение в роль.  
[DeputizedName](P_Tessa_Roles_RoleDeputyRecord_DeputizedName.htm)|  Имя
пользователя, замещение которого производится, или null, если производится не
замещение для конкретного пользователя, а временное включение в роль.  
[Deputy](P_Tessa_Roles_RoleDeputyRecord_Deputy.htm)|  Роль пользователя,
являющегося заместителем.  
[DeputyID](P_Tessa_Roles_RoleDeputyRecord_DeputyID.htm)|  Идентификатор
персональной роли пользователя, являющегося заместителем.  
[DeputyName](P_Tessa_Roles_RoleDeputyRecord_DeputyName.htm)|  Имя
пользователя, являющегося заместителем.  
[ID](P_Tessa_Platform_CollectionRecord_ID.htm)| Идентификатор записи.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
[IsActive](P_Tessa_Roles_RoleDeputyRecord_IsActive.htm)|  Признак того, что
замещение является активным.  
[IsEnabled](P_Tessa_Roles_RoleDeputyRecord_IsEnabled.htm)|  Признак того, что
замещение доступно, т.е. может стать активным. По умолчанию значение равно
true.  
[MaxDate](P_Tessa_Roles_RoleDeputyRecord_MaxDate.htm)|  Максимальная дата и
время, по завершении которых замещение перестаёт действовать, или
[MaxValue](https://learn.microsoft.com/dotnet/api/system.data.sqltypes.sqldatetime.maxvalue),
если замещение является постоянным.  
[MinDate](P_Tessa_Roles_RoleDeputyRecord_MinDate.htm)|  Минимальные дата и
время, начиная с которых замещение действует, или
[MinValue](https://learn.microsoft.com/dotnet/api/system.data.sqltypes.sqldatetime.minvalue),
если замещение является постоянным.  
[Role](P_Tessa_Roles_RoleDeputyRecord_Role.htm)|  Роль, для которой
определяются заместители.  
[RoleType](P_Tessa_Roles_RoleDeputyRecord_RoleType.htm)|  Тип роли, на которую
назначается замещение.  
[RowID](P_Tessa_Platform_CollectionRecord_RowID.htm)| Идентификатор объекта,
которому соответствует запись.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
##  __Методы
[Equals(ICollectionRecord)](M_Tessa_Platform_CollectionRecord_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
---|---  
[Equals(Object)](M_Tessa_Platform_CollectionRecord_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Platform_CollectionRecord_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Унаследован от [CollectionRecord](T_Tessa_Platform_CollectionRecord.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsActiveAt](M_Tessa_Roles_RoleDeputyRecord_IsActiveAt.htm)|  Возвращает
признак того, что замещение является активным в заданный момент.  
[IsPermanent](M_Tessa_Roles_RoleDeputyRecord_IsPermanent.htm)|  Возвращает
признак того, что замещение является постоянным.  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[SetPermanent](M_Tessa_Roles_RoleDeputyRecord_SetPermanent.htm)|
Устанавливает дату замещения таким образом, чтобы оно считалось постоянным.  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[UpdateFromAssociations](M_Tessa_Roles_RoleDeputyRecord_UpdateFromAssociations.htm)|
Обновляет значения ссылочных полей из всех объектов-ассоциаций, на которые
установлены ссылки.  
(Переопределяет
[CollectionRecord.UpdateFromAssociations()](M_Tessa_Platform_CollectionRecord_UpdateFromAssociations.htm))  
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
