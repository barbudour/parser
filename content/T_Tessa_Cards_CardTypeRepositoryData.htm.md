# CardTypeRepositoryData - класс
Объект, описывающий тип карточки в форме, пригодной для хранения в базе
данных.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public sealed class CardTypeRepositoryData : ICardSerializableEntry, 
    	INamedEntry, INamedItem, IEquatable<CardTypeRepositoryData>, IEquatable<CardType>
VB __Копировать
     Public NotInheritable Class CardTypeRepositoryData
    	Implements ICardSerializableEntry, INamedEntry, INamedItem, IEquatable(Of CardTypeRepositoryData), 
    	IEquatable(Of CardType)
C++ __Копировать
     public ref class CardTypeRepositoryData sealed : ICardSerializableEntry, 
    	INamedEntry, INamedItem, IEquatable<CardTypeRepositoryData^>, IEquatable<CardType^>
F# __Копировать
     [<SealedAttribute>]
    type CardTypeRepositoryData = 
        class
            interface ICardSerializableEntry
            interface INamedEntry
            interface INamedItem
            interface IEquatable<CardTypeRepositoryData>
            interface IEquatable<CardType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardTypeRepositoryData
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<CardTypeRepositoryData>, [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<[CardType](T_Tessa_Cards_CardType.htm)>, [ICardSerializableEntry](T_Tessa_Cards_ICardSerializableEntry.htm), [INamedItem](T_Tessa_Platform_Collections_INamedItem.htm), [INamedEntry](T_Tessa_Platform_INamedEntry.htm)
##  __Конструкторы
[CardTypeRepositoryData](M_Tessa_Cards_CardTypeRepositoryData__ctor.htm)|
Инициализирует новый экземпляр класса CardTypeRepositoryData  
---|---  
##  __Свойства
[Caption](P_Tessa_Cards_CardTypeRepositoryData_Caption.htm)|  Отображаемое в
пользовательском интерфейсе имя типа карточки.  
---|---  
[Flags](P_Tessa_Cards_CardTypeRepositoryData_Flags.htm)|  Флаги типа карточки.  
[Group](P_Tessa_Cards_CardTypeRepositoryData_Group.htm)|  Отображаемое в
пользовательском интерфейсе название группы для типа карточки. Может быть
равно null или пустой строке.  
[ID](P_Tessa_Cards_CardTypeRepositoryData_ID.htm)| Идентификатор объекта.  
[InstanceType](P_Tessa_Cards_CardTypeRepositoryData_InstanceType.htm)|  Тип
экземпляра карточки.  
[Metadata](P_Tessa_Cards_CardTypeRepositoryData_Metadata.htm)|  Строка,
содержащий другие поля объекта [CardType](T_Tessa_Cards_CardType.htm) в
формате типизированного json.  
[Name](P_Tessa_Cards_CardTypeRepositoryData_Name.htm)| Отображаемое имя
объекта.  
##  __Методы
[Equals(CardType)](M_Tessa_Cards_CardTypeRepositoryData_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(CardTypeRepositoryData)](M_Tessa_Cards_CardTypeRepositoryData_Equals_2.htm)|
Сравнивает текущий объект с заданным.  
[Equals(Object)](M_Tessa_Cards_CardTypeRepositoryData_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromCardType](M_Tessa_Cards_CardTypeRepositoryData_FromCardType.htm)|
Возвращает объект CardTypeRepositoryData, описывающий тип карточки в форме,
пригодной для хранения в базе данных.  
[GetHashCode](M_Tessa_Cards_CardTypeRepositoryData_GetHashCode.htm)|
Возвращает хеш-код объекта.  
(Переопределяет
[Object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode#system-
object-gethashcode))  
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
[ToCardType](M_Tessa_Cards_CardTypeRepositoryData_ToCardType.htm)|  Возвращает
объект [CardType](T_Tessa_Cards_CardType.htm), десериализованный из базы
данных.  
[ToString](M_Tessa_Cards_CardTypeRepositoryData_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
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
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
