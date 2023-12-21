# SchemeTable - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class SchemeTable : SchemeGroupableObject
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class SchemeTable
    	Inherits SchemeGroupableObject
C++ __Копировать
    [SerializableAttribute]
    public ref class SchemeTable sealed : public SchemeGroupableObject
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type SchemeTable = 
        class
            inherit SchemeGroupableObject
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm) __[SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm) __[SchemeGroupableObject](T_Tessa_Scheme_SchemeGroupableObject.htm) __ SchemeTable
##  __Конструкторы
[SchemeTable()](M_Tessa_Scheme_SchemeTable__ctor.htm)| Инициализирует новый
экземпляр класса SchemeTable  
Устарело.  
---|---  
[SchemeTable(String)](M_Tessa_Scheme_SchemeTable__ctor_4.htm)| Инициализирует
новый экземпляр класса SchemeTable  
[SchemeTable(Guid, String)](M_Tessa_Scheme_SchemeTable__ctor_1.htm)|
Инициализирует новый экземпляр класса SchemeTable  
[SchemeTable(String, SchemeTableInstanceType,
SchemeTableContentType)](M_Tessa_Scheme_SchemeTable__ctor_5.htm)|
Инициализирует новый экземпляр класса SchemeTable  
[SchemeTable(Guid, String, SchemeTableInstanceType,
SchemeTableContentType)](M_Tessa_Scheme_SchemeTable__ctor_2.htm)|
Инициализирует новый экземпляр класса SchemeTable  
[SchemeTable(String, SchemeTableInstanceType, SchemeTableContentType,
SchemeNamedObject[])](M_Tessa_Scheme_SchemeTable__ctor_6.htm)| Инициализирует
новый экземпляр класса SchemeTable  
[SchemeTable(Guid, String, SchemeTableInstanceType, SchemeTableContentType,
SchemeNamedObject[])](M_Tessa_Scheme_SchemeTable__ctor_3.htm)| Инициализирует
новый экземпляр класса SchemeTable  
##  __Свойства
[Columns](P_Tessa_Scheme_SchemeTable_Columns.htm)|  
---|---  
[Constraints](P_Tessa_Scheme_SchemeTable_Constraints.htm)|  
[ContentType](P_Tessa_Scheme_SchemeTable_ContentType.htm)|  
[Database](P_Tessa_Scheme_SchemeTable_Database.htm)|  
[Description](P_Tessa_Scheme_SchemeNamedObject_Description.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Group](P_Tessa_Scheme_SchemeGroupableObject_Group.htm)|  
(Унаследован от
[SchemeGroupableObject](T_Tessa_Scheme_SchemeGroupableObject.htm))  
[HasSystemControlledName](P_Tessa_Scheme_SchemeNamedObject_HasSystemControlledName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[ID](P_Tessa_Scheme_SchemeNamedObject_ID.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Indexes](P_Tessa_Scheme_SchemeTable_Indexes.htm)|  
[InstanceType](P_Tessa_Scheme_SchemeTable_InstanceType.htm)|  
[IsPartitionInherited](P_Tessa_Scheme_SchemePartionableObject_IsPartitionInherited.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsVirtual](P_Tessa_Scheme_SchemeTable_IsVirtual.htm)|  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Name](P_Tessa_Scheme_SchemeNamedObject_Name.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[Records](P_Tessa_Scheme_SchemeTable_Records.htm)|  
## __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeNamedObject_BeginDeserializationOverride.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
---|---  
[Copy(SchemeObject)](M_Tessa_Scheme_SchemeTable_Copy.htm)|  
(Переопределяет
[SchemeGroupableObject.Copy(SchemeObject)](M_Tessa_Scheme_SchemeGroupableObject_Copy.htm))  
[Copy(SchemeObject, Boolean)](M_Tessa_Scheme_SchemeTable_Copy_1.htm)|  
[CreateStoreScope](M_Tessa_Scheme_SchemeTable_CreateStoreScope.htm)|  Создает
скоуп, внтри которого не осуществляется проверка имен объектов  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemeTable_EndDeserializationOverride.htm)|  
(Переопределяет
[SchemeGroupableObject.EndDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemeGroupableObject_EndDeserializationOverride.htm))  
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
[Find](M_Tessa_Scheme_SchemeTable_Find.htm)|  
[GetDisplayName](M_Tessa_Scheme_SchemeNamedObject_GetDisplayName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemeTable_GetInheritedPartition.htm)|  
(Переопределяет
[SchemePartionableObject.GetInheritedPartition(SchemeObject)](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm))  
[GetObjectData](M_Tessa_Scheme_SchemeTable_GetObjectData.htm)|  
(Переопределяет
[SchemeGroupableObject.GetObjectData(SerializationInfo)](M_Tessa_Scheme_SchemeGroupableObject_GetObjectData.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsInvalidPartition](M_Tessa_Scheme_SchemePartionableObject_IsInvalidPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[IsParentColumn](M_Tessa_Scheme_SchemeTable_IsParentColumn.htm)|  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnSealed](M_Tessa_Scheme_SchemeTable_OnSealed.htm)|  
(Переопределяет
[SchemeObject.OnSealed()](M_Tessa_Scheme_SchemeObject_OnSealed.htm))  
[RaisePropertyChanged](M_Tessa_Scheme_SchemeObject_RaisePropertyChanged.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(String)](M_Tessa_Scheme_SchemeObject_ReadXml.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(XmlReader)](M_Tessa_Scheme_SchemeObject_ReadXml_1.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Seal](M_Tessa_Scheme_SchemeObject_Seal.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ToString](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring)| Returns a string that represents the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[WriteXml](M_Tessa_Scheme_SchemeObject_WriteXml.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
##  __События
[PropertyChanged](E_Tessa_Scheme_SchemeObject_PropertyChanged.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
---|---  
##  __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetReferencedTables](M_Tessa_Scheme_SchemeTableExtensions_GetReferencedTables.htm)|  
(Определяется
[SchemeTableExtensions](T_Tessa_Scheme_SchemeTableExtensions.htm))  
[GetReferencingTables](M_Tessa_Scheme_SchemeTableExtensions_GetReferencingTables.htm)|  
(Определяется
[SchemeTableExtensions](T_Tessa_Scheme_SchemeTableExtensions.htm))  
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
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
