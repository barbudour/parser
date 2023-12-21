# CardFileSourceType - структура
Местоположение контента файла.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public readonly struct CardFileSourceType : IEquatable<CardFileSourceType>
VB __Копировать
     Public Structure CardFileSourceType
    	Implements IEquatable(Of CardFileSourceType)
C++ __Копировать
     public value class CardFileSourceType : IEquatable<CardFileSourceType>
F# __Копировать
     [<SealedAttribute>]
    type CardFileSourceType = 
        struct
            inherit ValueType
            interface IEquatable<CardFileSourceType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __[ValueType](https://learn.microsoft.com/dotnet/api/system.valuetype) __ CardFileSourceType
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<CardFileSourceType>
##  __Конструкторы
[CardFileSourceType](M_Tessa_Cards_CardFileSourceType__ctor.htm)|  Создаёт
экземпляр местоположения контента файла с указанием его идентификатора.  
---|---  
## __Свойства
[ID](P_Tessa_Cards_CardFileSourceType_ID.htm)|  Идентификатор местоположения.  
---|---  
## __Методы
[Equals(CardFileSourceType)](M_Tessa_Cards_CardFileSourceType_Equals_1.htm)|
Сравнивает текущий объект с заданным.  
---|---  
[Equals(Object)](M_Tessa_Cards_CardFileSourceType_Equals.htm)| Сравнивает
текущий объект с заданным.  
(Переопределяет
[ValueType.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.valuetype.equals#system-
valuetype-equals\(system-object\)))  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[GetHashCode](M_Tessa_Cards_CardFileSourceType_GetHashCode.htm)| Возвращает
хеш-код объекта.  
(Переопределяет
[ValueType.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.valuetype.gethashcode#system-
valuetype-gethashcode))  
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
[ToString](M_Tessa_Cards_CardFileSourceType_ToString.htm)| Возвращает
строковое представление объекта.  
(Переопределяет
[ValueType.ToString()](https://learn.microsoft.com/dotnet/api/system.valuetype.tostring#system-
valuetype-tostring))  
##  __Операторы
[Equality(CardFileSourceType,
CardFileSourceType)](M_Tessa_Cards_CardFileSourceType_op_Equality.htm)|
Сравнивает заданные значения на равенство.  
---|---  
[Explicit(CardFileSourceType to
Int32)](M_Tessa_Cards_CardFileSourceType_op_Explicit_1.htm)|  
[Explicit(Int32 to
CardFileSourceType)](M_Tessa_Cards_CardFileSourceType_op_Explicit.htm)|  
[Inequality(CardFileSourceType,
CardFileSourceType)](M_Tessa_Cards_CardFileSourceType_op_Inequality.htm)|
Сравнивает заданные значения на неравенство.  
##  __Поля
[Database](F_Tessa_Cards_CardFileSourceType_Database.htm)|  Контент файла
размещается в базе данных. Такое местоположение принято в системе с
настройками по умолчанию и может не соответствовать действительным настройкам
сервера.  
---|---  
[DefaultDatabasePath](F_Tessa_Cards_CardFileSourceType_DefaultDatabasePath.htm)|
Путь к местоположению контента файла в базе данных по умолчанию. Может не
соответствовать конфигурационной строке с именем "default".  
[FileSystem](F_Tessa_Cards_CardFileSourceType_FileSystem.htm)|  Контент файла
размещается в файловой системе. Такое местоположение принято в системе с
настройками по умолчанию и может не соответствовать действительным настройкам
сервера.  
## __Методы расширения
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
