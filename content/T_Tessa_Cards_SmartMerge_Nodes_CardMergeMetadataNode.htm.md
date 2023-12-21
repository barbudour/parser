# CardMergeMetadataNode - класс
##  __Definition
 **Пространство имён:**
[Tessa.Cards.SmartMerge.Nodes](N_Tessa_Cards_SmartMerge_Nodes.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardMergeMetadataNode : IMergeMetadataNode
VB __Копировать
     Public Class CardMergeMetadataNode
    	Implements IMergeMetadataNode
C++ __Копировать
     public ref class CardMergeMetadataNode : IMergeMetadataNode
F# __Копировать
     type CardMergeMetadataNode = 
        class
            interface IMergeMetadataNode
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMergeMetadataNode
Implements
    [IMergeMetadataNode](T_Tessa_SmartMerge_IMergeMetadataNode.htm)
##  __Конструкторы
[CardMergeMetadataNode](M_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode__ctor.htm)|
Инициализирует новый экземпляр класса CardMergeMetadataNode  
---|---  
##  __Свойства
[CardID](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_CardID.htm)|  ID
карточки к которой относится данный узел.  
---|---  
[FileContentColumns](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_FileContentColumns.htm)|
Список полей, по которым определяется изменен ли контент файла.  
[FileIncludedColumns](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_FileIncludedColumns.htm)|
Включенные колонки. Если заполнены, то значения узлов слияния для файлов,
будут сравниваться только с учетом этих колонок.  
[IgnoreDuplicateRows](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_IgnoreDuplicateRows.htm)|
Флаг, влияющий на логику при обнаружении дубликатов узлов, например, на втором
уровне сопоставления, несколько узлов имеют одинаковые значения `KeyColumns`.  
[IsIgnored](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_IsIgnored.htm)|
Флаг, указывающий на то будет ли игнорироваться данный узел дальнейшей логикой
слияния.  
[KeyColumns](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_KeyColumns.htm)|
Список ключевых колонок в секции, если заданы, эти колонки будут задействованы
для 2-го уровня сопосталвения.  
[MetaType](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_MetaType.htm)|
Тип узла метаданных слияния.  
[SectionIgnoredForEqualsColumns](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_SectionIgnoredForEqualsColumns.htm)|
Список колонок в секции, которые будут игнорированы при сравнении узлов по
значению.  
[SectionIgnoredForModifyColumns](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_SectionIgnoredForModifyColumns.htm)|
Список колонок в секции, которые будут игнорированы для изменения.  
[SectionName](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_SectionName.htm)|
Наименование секции карточки.  
[SectionParentColumnName](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_SectionParentColumnName.htm)|
Наименование колонки в секции, являющейся указателем на строку в родительской
секции.  
[SectionParentName](P_Tessa_Cards_SmartMerge_Nodes_CardMergeMetadataNode_SectionParentName.htm)|
Наименование родительской секции, относительно секции указанной в
`SectionName`.  
## __Методы
[Equals](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\))| Determines whether the specified object is
equal to the current object.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
---|---  
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
[Tessa.Cards.SmartMerge.Nodes - пространство
имён](N_Tessa_Cards_SmartMerge_Nodes.htm)
