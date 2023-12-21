# SchemeComplexColumn - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class SchemeComplexColumn : SchemeColumn
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class SchemeComplexColumn
    	Inherits SchemeColumn
C++ __Копировать
    [SerializableAttribute]
    public ref class SchemeComplexColumn sealed : public SchemeColumn
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type SchemeComplexColumn = 
        class
            inherit SchemeColumn
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm) __[SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm) __[SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm) __ SchemeComplexColumn
##  __Конструкторы
[SchemeComplexColumn()](M_Tessa_Scheme_SchemeComplexColumn__ctor.htm)|
Инициализирует новый экземпляр класса SchemeComplexColumn  
Устарело.  
---|---  
[SchemeComplexColumn(String,
SchemeType)](M_Tessa_Scheme_SchemeComplexColumn__ctor_4.htm)| Инициализирует
новый экземпляр класса SchemeComplexColumn  
[SchemeComplexColumn(Guid, String,
SchemeType)](M_Tessa_Scheme_SchemeComplexColumn__ctor_1.htm)| Инициализирует
новый экземпляр класса SchemeComplexColumn  
[SchemeComplexColumn(String, SchemeType,
SchemeTable)](M_Tessa_Scheme_SchemeComplexColumn__ctor_5.htm)| Инициализирует
новый экземпляр класса SchemeComplexColumn  
[SchemeComplexColumn(Guid, String, SchemeType,
SchemeTable)](M_Tessa_Scheme_SchemeComplexColumn__ctor_2.htm)| Инициализирует
новый экземпляр класса SchemeComplexColumn  
[SchemeComplexColumn(String, SchemeType, SchemeTable,
SchemePhysicalColumn[])](M_Tessa_Scheme_SchemeComplexColumn__ctor_6.htm)|
Инициализирует новый экземпляр класса SchemeComplexColumn  
[SchemeComplexColumn(Guid, String, SchemeType, SchemeTable,
SchemePhysicalColumn[])](M_Tessa_Scheme_SchemeComplexColumn__ctor_3.htm)|
Инициализирует новый экземпляр класса SchemeComplexColumn  
##  __Свойства
[Columns](P_Tessa_Scheme_SchemeComplexColumn_Columns.htm)|  
---|---  
[Description](P_Tessa_Scheme_SchemeNamedObject_Description.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[ForeignKey](P_Tessa_Scheme_SchemeComplexColumn_ForeignKey.htm)|  
[HasSystemControlledName](P_Tessa_Scheme_SchemeNamedObject_HasSystemControlledName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[HasSystemControlledType](P_Tessa_Scheme_SchemeColumn_HasSystemControlledType.htm)|  
(Унаследован от [SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm))  
[ID](P_Tessa_Scheme_SchemeNamedObject_ID.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[IsPartitionInherited](P_Tessa_Scheme_SchemePartionableObject_IsPartitionInherited.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsReferenceToOwner](P_Tessa_Scheme_SchemeComplexColumn_IsReferenceToOwner.htm)|  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Name](P_Tessa_Scheme_SchemeNamedObject_Name.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[ReferencedTable](P_Tessa_Scheme_SchemeComplexColumn_ReferencedTable.htm)|  
[ShouldRequirePrefix](P_Tessa_Scheme_SchemeComplexColumn_ShouldRequirePrefix.htm)|  
[Table](P_Tessa_Scheme_SchemeColumn_Table.htm)|  
(Унаследован от [SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm))  
[Type](P_Tessa_Scheme_SchemeColumn_Type.htm)|  
(Унаследован от [SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm))  
[WithForeignKey](P_Tessa_Scheme_SchemeComplexColumn_WithForeignKey.htm)|  
## __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeComplexColumn_BeginDeserializationOverride.htm)|  
(Переопределяет
[SchemeColumn.BeginDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemeColumn_BeginDeserializationOverride.htm))  
---|---  
[Copy](M_Tessa_Scheme_SchemeComplexColumn_Copy.htm)|  
(Переопределяет
[SchemeColumn.Copy(SchemeObject)](M_Tessa_Scheme_SchemeColumn_Copy.htm))  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemeComplexColumn_EndDeserializationOverride.htm)|  
(Переопределяет
[SchemePartionableObject.EndDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemePartionableObject_EndDeserializationOverride.htm))  
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
[GetDisplayName](M_Tessa_Scheme_SchemeNamedObject_GetDisplayName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[GetObjectData](M_Tessa_Scheme_SchemeComplexColumn_GetObjectData.htm)|  
(Переопределяет
[SchemeColumn.GetObjectData(SerializationInfo)](M_Tessa_Scheme_SchemeColumn_GetObjectData.htm))  
[GetType](https://learn.microsoft.com/dotnet/api/system.object.gettype#system-
object-gettype)| Gets the
[Type](https://learn.microsoft.com/dotnet/api/system.type) of the current
instance.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[IsInvalidPartition](M_Tessa_Scheme_SchemePartionableObject_IsInvalidPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[MemberwiseClone](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone#system-
object-memberwiseclone)| Creates a shallow copy of the current
[Object](https://learn.microsoft.com/dotnet/api/system.object).  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[OnSealed](M_Tessa_Scheme_SchemeComplexColumn_OnSealed.htm)|  
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
[SetReferencedTable](M_Tessa_Scheme_SchemeComplexColumn_SetReferencedTable.htm)|  
[SetType](M_Tessa_Scheme_SchemeComplexColumn_SetType.htm)|  
(Переопределяет
[SchemeColumn.SetType(SchemeType)](M_Tessa_Scheme_SchemeColumn_SetType.htm))  
[ToString](M_Tessa_Scheme_SchemeColumn_ToString.htm)|  
(Унаследован от [SchemeColumn](T_Tessa_Scheme_SchemeColumn.htm))  
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
