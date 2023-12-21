# SchemeDatabase - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    public sealed class SchemeDatabase : SchemeNamedObject, 
    	ISchemeService
VB __Копировать
    <SerializableAttribute>
    Public NotInheritable Class SchemeDatabase
    	Inherits SchemeNamedObject
    	Implements ISchemeService
C++ __Копировать
    [SerializableAttribute]
    public ref class SchemeDatabase sealed : public SchemeNamedObject, 
    	ISchemeService
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    type SchemeDatabase = 
        class
            inherit SchemeNamedObject
            interface ISchemeService
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[SchemeObject](T_Tessa_Scheme_SchemeObject.htm) __[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm) __[SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm) __ SchemeDatabase
Implements
    [ISchemeService](T_Tessa_Scheme_ISchemeService.htm)
##  __Конструкторы
[SchemeDatabase()](M_Tessa_Scheme_SchemeDatabase__ctor.htm)| Инициализирует
новый экземпляр класса SchemeDatabase  
Устарело.  
---|---  
[SchemeDatabase(String)](M_Tessa_Scheme_SchemeDatabase__ctor_2.htm)|
Инициализирует новый экземпляр класса SchemeDatabase  
[SchemeDatabase(Guid, String, Boolean,
Boolean)](M_Tessa_Scheme_SchemeDatabase__ctor_1.htm)| Инициализирует новый
экземпляр класса SchemeDatabase  
##  __Свойства
[Collation](P_Tessa_Scheme_SchemeDatabase_Collation.htm)|  
---|---  
[Current](P_Tessa_Scheme_SchemeDatabase_Current.htm)|  
[Description](P_Tessa_Scheme_SchemeNamedObject_Description.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Functions](P_Tessa_Scheme_SchemeDatabase_Functions.htm)|  
[HasSystemControlledName](P_Tessa_Scheme_SchemeNamedObject_HasSystemControlledName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[ID](P_Tessa_Scheme_SchemeNamedObject_ID.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[IsPartitionInherited](P_Tessa_Scheme_SchemePartionableObject_IsPartitionInherited.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[IsPermanent](P_Tessa_Scheme_SchemeObject_IsPermanent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSealed](P_Tessa_Scheme_SchemeObject_IsSealed.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[IsSystem](P_Tessa_Scheme_SchemeObject_IsSystem.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[LinkedWith](P_Tessa_Scheme_SchemeObject_LinkedWith.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Migrations](P_Tessa_Scheme_SchemeDatabase_Migrations.htm)|  
[Modified](P_Tessa_Scheme_SchemeDatabase_Modified.htm)|  
[ModifiedByID](P_Tessa_Scheme_SchemeDatabase_ModifiedByID.htm)|  
[ModifiedByName](P_Tessa_Scheme_SchemeDatabase_ModifiedByName.htm)|  
[Name](P_Tessa_Scheme_SchemeNamedObject_Name.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[Parent](P_Tessa_Scheme_SchemeObject_Parent.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[Partition](P_Tessa_Scheme_SchemePartionableObject_Partition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[Partitions](P_Tessa_Scheme_SchemeDatabase_Partitions.htm)|  
[Procedures](P_Tessa_Scheme_SchemeDatabase_Procedures.htm)|  
[Tables](P_Tessa_Scheme_SchemeDatabase_Tables.htm)|  
## __Методы
[BeginDeserializationOverride](M_Tessa_Scheme_SchemeDatabase_BeginDeserializationOverride.htm)|  
(Переопределяет
[SchemeNamedObject.BeginDeserializationOverride(SerializationInfo)](M_Tessa_Scheme_SchemeNamedObject_BeginDeserializationOverride.htm))  
---|---  
[Copy](M_Tessa_Scheme_SchemeDatabase_Copy.htm)|  
(Переопределяет
[SchemeNamedObject.Copy(SchemeObject)](M_Tessa_Scheme_SchemeNamedObject_Copy.htm))  
[Deserialize](M_Tessa_Scheme_SchemeObject_Deserialize.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[EndDeserializationOverride](M_Tessa_Scheme_SchemeDatabase_EndDeserializationOverride.htm)|  
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
[FromXml(String)](M_Tessa_Scheme_SchemeDatabase_FromXml.htm)|  
[FromXml(XmlReader)](M_Tessa_Scheme_SchemeDatabase_FromXml_1.htm)|  
[GetDisplayName](M_Tessa_Scheme_SchemeNamedObject_GetDisplayName.htm)|  
(Унаследован от [SchemeNamedObject](T_Tessa_Scheme_SchemeNamedObject.htm))  
[GetHashCode](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode)| Serves as the default hash function.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetInheritedPartition](M_Tessa_Scheme_SchemePartionableObject_GetInheritedPartition.htm)|  
(Унаследован от
[SchemePartionableObject](T_Tessa_Scheme_SchemePartionableObject.htm))  
[GetObjectData](M_Tessa_Scheme_SchemeDatabase_GetObjectData.htm)|  
(Переопределяет
[SchemeNamedObject.GetObjectData(SerializationInfo)](M_Tessa_Scheme_SchemeNamedObject_GetObjectData.htm))  
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
[OnSealed](M_Tessa_Scheme_SchemeDatabase_OnSealed.htm)|  
(Переопределяет
[SchemeObject.OnSealed()](M_Tessa_Scheme_SchemeObject_OnSealed.htm))  
[RaisePropertyChanged](M_Tessa_Scheme_SchemeObject_RaisePropertyChanged.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(String)](M_Tessa_Scheme_SchemeObject_ReadXml.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[ReadXml(XmlReader)](M_Tessa_Scheme_SchemeObject_ReadXml_1.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[RefreshAsync](M_Tessa_Scheme_SchemeDatabase_RefreshAsync.htm)|  
[Seal](M_Tessa_Scheme_SchemeObject_Seal.htm)|  
(Унаследован от [SchemeObject](T_Tessa_Scheme_SchemeObject.htm))  
[SubmitChangesAsync](M_Tessa_Scheme_SchemeDatabase_SubmitChangesAsync.htm)|  
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
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_3.htm)|
Выполняет проверку наличия таблицы с идентификатором tableID в схеме.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
[ValidateAsync](M_Tessa_UI_Cards_CardUIExtensions_ValidateAsync_2.htm)|
Выполняет проверку наличия колонки с идентификатором columnID в таблице с
идентификатором tableID.  
(Определяется [CardUIExtensions](T_Tessa_UI_Cards_CardUIExtensions.htm))  
##  __См. также
#### Ссылки
[Tessa.Scheme - пространство имён](N_Tessa_Scheme.htm)
