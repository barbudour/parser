# CardMetadataBuilderBase.ColumnContainerInfo - класс
Информация по физической или комплексной колонке, которая необходима для
построения объекта [CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) в
методе [BuildAsync(CardTypeCollection, ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected sealed class ColumnContainerInfo
VB __Копировать
     Protected NotInheritable Class ColumnContainerInfo
C++ __Копировать
     protected ref class ColumnContainerInfo sealed
F# __Копировать
     [<SealedAttribute>]
    type ColumnContainerInfo = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataBuilderBase.ColumnContainerInfo
##  __Конструкторы
[CardMetadataBuilderBase.ColumnContainerInfo](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo__ctor.htm)|
Создаёт экземпляр класса с указанием максимально допустимого числа типов
карточек, информацию о которых может содержать одна колонка.  
---|---  
## __Свойства
[CardTypeCount](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_CardTypeCount.htm)|
Количество типов карточек  
---|---  
[CardTypeIDs](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_CardTypeIDs.htm)|
Массив идентификаторов типов карточек, в которых используется текущая колонка.
Только
[CardTypeCount](P_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_CardTypeCount.htm)
первых элементов массива заполнены действительными значениями. Для добавления
идентификаторов в массив следует использовать метод
[AddCardTypeID(Guid)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_AddCardTypeID.htm).  
## __Методы
[AddCardTypeID](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_AddCardTypeID.htm)|
Добавляет информацию о том, что текущая колонка используется в типе карточки с
заданным идентификатором.  
---|---  
[CreateCardTypeIDList](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_ColumnContainerInfo_CreateCardTypeIDList.htm)|
Возвращает список идентификаторов типов карточек, в которых используется
текущая колонка.  
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
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
