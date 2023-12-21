# CardMetadataAllTablesBuilder - класс
Объект, выполняющий построение метаинформации для всех таблиц, вне зависимости
от их использования в типах карточек, на основании информации, которая
описывается коллекцией [SchemeItems](P_Tessa_Cards_CardType_SchemeItems.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public class CardMetadataAllTablesBuilder : CardMetadataBuilder
VB __Копировать
     Public Class CardMetadataAllTablesBuilder
    	Inherits CardMetadataBuilder
C++ __Копировать
     public ref class CardMetadataAllTablesBuilder : public CardMetadataBuilder
F# __Копировать
     type CardMetadataAllTablesBuilder = 
        class
            inherit CardMetadataBuilder
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[CardMetadataBuilderBase](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm) __[CardMetadataBuilder](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm) __ CardMetadataAllTablesBuilder
##  __Конструкторы
[CardMetadataAllTablesBuilder()](M_Tessa_Cards_Metadata_CardMetadataAllTablesBuilder__ctor.htm)|
Initializes a new instance of the
[Object](https://learn.microsoft.com/dotnet/api/system.object) class.  
---|---  
[CardMetadataAllTablesBuilder(Func<ICardMetadataExtensionExecutor>)](M_Tessa_Cards_Metadata_CardMetadataAllTablesBuilder__ctor_1.htm)|
Создаёт экземпляр класса с указанием его зависимостей.  
## __Методы
[AddCardTypeAsync](M_Tessa_Cards_Metadata_CardMetadataBuilder_AddCardTypeAsync.htm)|
Добавляет информацию по секциям и колонкам заданного типа карточки в контейнер
[Tessa.Cards.Metadata.CardMetadataBuilderBase.MetadataContainer].  
(Унаследован от
[CardMetadataBuilder](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm))  
---|---  
[BuildAsync](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildAsync.htm)|
Выполняет построение метаинформации
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) по заданным типам
карточек cardTypes и возвращает созданный объект.  
(Унаследован от
[CardMetadataBuilderBase](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm))  
[BuildInternalAsync](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_BuildInternalAsync.htm)|
Выполняет построение метаинформации
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm) по заданным типам
карточек cardTypes и возвращает созданный объект.  
(Унаследован от
[CardMetadataBuilderBase](T_Tessa_Cards_Metadata_CardMetadataBuilderBase.htm))  
[CheckCardType](M_Tessa_Cards_Metadata_CardMetadataBuilder_CheckCardType.htm)|
Проверяет информацию по секциям и колонкам заданного типа карточки после
построения метаинформации, если расширения запросили отложить проверку для
этого типа карточки.  
(Унаследован от
[CardMetadataBuilder](T_Tessa_Cards_Metadata_CardMetadataBuilder.htm))  
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
[PrepareContainerInternalAsync](M_Tessa_Cards_Metadata_CardMetadataAllTablesBuilder_PrepareContainerInternalAsync.htm)|
Подготавливает контейнер метаинформации
[CardMetadataBuilderBase.MetadataContainer](T_Tessa_Cards_Metadata_CardMetadataBuilderBase_MetadataContainer.htm)
перед построением мета информации для карточек
[CardMetadata](T_Tessa_Cards_Metadata_CardMetadata.htm).  
(Переопределяет
[CardMetadataBuilderBase.PrepareContainerInternalAsync(CardMetadataBuilderBase.MetadataContainer,
ISchemeService,
CancellationToken)](M_Tessa_Cards_Metadata_CardMetadataBuilderBase_PrepareContainerInternalAsync.htm))  
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
