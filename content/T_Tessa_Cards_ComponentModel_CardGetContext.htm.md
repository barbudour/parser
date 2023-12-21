# CardGetContext - класс
Контекст операции по загрузке карточки.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardGetContext
VB __Копировать
     Public NotInheritable Class CardGetContext
C++ __Копировать
     public ref class CardGetContext sealed
F# __Копировать
     [<SealedAttribute>]
    type CardGetContext = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardGetContext
##  __Конструкторы
[CardGetContext](M_Tessa_Cards_ComponentModel_CardGetContext__ctor.htm)|
Создаёт экземпляр класса с указанием информации, необходимой для загрузки
карточки.  
---|---  
## __Свойства
[Card](P_Tessa_Cards_ComponentModel_CardGetContext_Card.htm)|  Загружаемая
карточка.  
---|---  
[CardID](P_Tessa_Cards_ComponentModel_CardGetContext_CardID.htm)|
Идентификатор загружаемой карточки.  
[CardMetadata](P_Tessa_Cards_ComponentModel_CardGetContext_CardMetadata.htm)|
Метаинформация по типу загружаемой карточки.  
[CardTypeID](P_Tessa_Cards_ComponentModel_CardGetContext_CardTypeID.htm)|  Тип
загружаемой карточки.  
[Db](P_Tessa_Cards_ComponentModel_CardGetContext_Db.htm)|  Объект,
осуществляющий взаимодействие с базой данных.  
[NewMode](P_Tessa_Cards_ComponentModel_CardGetContext_NewMode.htm)|  Способ
заполнения данных для виртуальных секций.  
[SectionsToExclude](P_Tessa_Cards_ComponentModel_CardGetContext_SectionsToExclude.htm)|
Список идентификаторов физических секций, загрузку которых не следует
выполнять. Не влияет на виртуальные секции.  
[ValidationResult](P_Tessa_Cards_ComponentModel_CardGetContext_ValidationResult.htm)|
Объект, выполняющий построение результата валидации.  
[WarningIfEntryNotFound](P_Tessa_Cards_ComponentModel_CardGetContext_WarningIfEntryNotFound.htm)|
Флаг, указывающий на то, что в случае отсутствия строковой секции в БД, будет
сгенерировано предупреждение, а не ошибка.  
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
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
