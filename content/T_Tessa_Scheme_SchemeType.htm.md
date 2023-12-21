# SchemeType - класс
##  __Definition
 **Пространство имён:** [Tessa.Scheme](N_Tessa_Scheme.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
    [SerializableAttribute]
    [TypeConverterAttribute(typeof(SchemeTypeConverter))]
    public sealed class SchemeType : IEquatable<SchemeType>
VB __Копировать
    <SerializableAttribute>
    <TypeConverterAttribute(GetType(SchemeTypeConverter))>
    Public NotInheritable Class SchemeType
    	Implements IEquatable(Of SchemeType)
C++ __Копировать
    [SerializableAttribute]
    [TypeConverterAttribute(typeof(SchemeTypeConverter))]
    public ref class SchemeType sealed : IEquatable<SchemeType^>
F# __Копировать
     [<SealedAttribute>]
    [<SerializableAttribute>]
    [<TypeConverterAttribute(typeof(SchemeTypeConverter))>]
    type SchemeType = 
        class
            interface IEquatable<SchemeType>
        end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ SchemeType
Implements
    [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)<SchemeType>
##  __Конструкторы
[SchemeType(SchemeType, Boolean)](M_Tessa_Scheme_SchemeType__ctor.htm)|
Инициализирует новый экземпляр класса SchemeType  
---|---  
[SchemeType(SchemeType, Byte)](M_Tessa_Scheme_SchemeType__ctor_1.htm)|
Инициализирует новый экземпляр класса SchemeType  
[SchemeType(SchemeType, Int64)](M_Tessa_Scheme_SchemeType__ctor_5.htm)|
Инициализирует новый экземпляр класса SchemeType  
[SchemeType(SchemeType, Byte,
Boolean)](M_Tessa_Scheme_SchemeType__ctor_2.htm)| Инициализирует новый
экземпляр класса SchemeType  
[SchemeType(SchemeType, Byte, Byte)](M_Tessa_Scheme_SchemeType__ctor_3.htm)|
Инициализирует новый экземпляр класса SchemeType  
[SchemeType(SchemeType, Int64,
Boolean)](M_Tessa_Scheme_SchemeType__ctor_6.htm)| Инициализирует новый
экземпляр класса SchemeType  
[SchemeType(SchemeType, Byte, Byte,
Boolean)](M_Tessa_Scheme_SchemeType__ctor_4.htm)| Инициализирует новый
экземпляр класса SchemeType  
##  __Свойства
[ClrType](P_Tessa_Scheme_SchemeType_ClrType.htm)|  
---|---  
[DbType](P_Tessa_Scheme_SchemeType_DbType.htm)|  
[HasLength](P_Tessa_Scheme_SchemeType_HasLength.htm)|  
[HasMaxLength](P_Tessa_Scheme_SchemeType_HasMaxLength.htm)|  
[HasPrecision](P_Tessa_Scheme_SchemeType_HasPrecision.htm)|  
[HasScale](P_Tessa_Scheme_SchemeType_HasScale.htm)|  
[IsAbstractReference](P_Tessa_Scheme_SchemeType_IsAbstractReference.htm)|  
[IsIntegerType](P_Tessa_Scheme_SchemeType_IsIntegerType.htm)|  Признак того,
что тип можно трактовать как целое число. Для целочисленных типов доступны
дополнительные настройки в редакторе, сейчас это возможность указать Identity
для автоматической нумерации строк.  
[IsNullable](P_Tessa_Scheme_SchemeType_IsNullable.htm)|  
[IsReference](P_Tessa_Scheme_SchemeType_IsReference.htm)|  
[IsStringType](P_Tessa_Scheme_SchemeType_IsStringType.htm)|  Признак того, что
тип можно трактовать как строку. Для строки доступны дополнительные настройки
в редакторе, сейчас это возможность указать Collation для колонки, и
возможность задать функцию lower для индекса в Postgres.  
[IsTypifiedReference](P_Tessa_Scheme_SchemeType_IsTypifiedReference.htm)|  
[Length](P_Tessa_Scheme_SchemeType_Length.htm)|  
[Name](P_Tessa_Scheme_SchemeType_Name.htm)|  
[Precision](P_Tessa_Scheme_SchemeType_Precision.htm)|  
[Scale](P_Tessa_Scheme_SchemeType_Scale.htm)|  
## __Методы
[Equals(Object)](M_Tessa_Scheme_SchemeType_Equals.htm)|  
(Переопределяет
[Object.Equals(Object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-
object-equals\(system-object\)))  
---|---  
[Equals(SchemeType)](M_Tessa_Scheme_SchemeType_Equals_1.htm)|  
[Finalize](https://learn.microsoft.com/dotnet/api/system.object.finalize#system-
object-finalize)| Allows an object to try to free resources and perform other
cleanup operations before it is reclaimed by garbage collection.  
(Унаследован от
[Object](https://learn.microsoft.com/dotnet/api/system.object))  
[FromType](M_Tessa_Scheme_SchemeType_FromType.htm)|  
[GetHashCode](M_Tessa_Scheme_SchemeType_GetHashCode.htm)|  
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
[Parse(String)](M_Tessa_Scheme_SchemeType_Parse.htm)|  
[Parse(String, Boolean)](M_Tessa_Scheme_SchemeType_Parse_1.htm)|  
[ToString](M_Tessa_Scheme_SchemeType_ToString.htm)|  
(Переопределяет
[Object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring#system-
object-tostring))  
[TryParse(String, SchemeType)](M_Tessa_Scheme_SchemeType_TryParse_1.htm)|  
[TryParse(String, Boolean,
SchemeType)](M_Tessa_Scheme_SchemeType_TryParse.htm)|  
## __Операторы
[Equality(SchemeType, SchemeType)](M_Tessa_Scheme_SchemeType_op_Equality.htm)|  
---|---  
[Inequality(SchemeType,
SchemeType)](M_Tessa_Scheme_SchemeType_op_Inequality.htm)|  
## __Поля
[AnsiString](F_Tessa_Scheme_SchemeType_AnsiString.htm)|  
---|---  
[AnsiStringFixedLength](F_Tessa_Scheme_SchemeType_AnsiStringFixedLength.htm)|  
[Binary](F_Tessa_Scheme_SchemeType_Binary.htm)|  
[BinaryJson](F_Tessa_Scheme_SchemeType_BinaryJson.htm)|  
[Boolean](F_Tessa_Scheme_SchemeType_Boolean.htm)|  
[Byte](F_Tessa_Scheme_SchemeType_Byte.htm)|  
[Currency](F_Tessa_Scheme_SchemeType_Currency.htm)|  
[Date](F_Tessa_Scheme_SchemeType_Date.htm)|  
[DateTime](F_Tessa_Scheme_SchemeType_DateTime.htm)|  
[DateTime2](F_Tessa_Scheme_SchemeType_DateTime2.htm)|  
[DateTimeOffset](F_Tessa_Scheme_SchemeType_DateTimeOffset.htm)|  
[Decimal](F_Tessa_Scheme_SchemeType_Decimal.htm)|  
[Double](F_Tessa_Scheme_SchemeType_Double.htm)|  
[Guid](F_Tessa_Scheme_SchemeType_Guid.htm)|  
[Int16](F_Tessa_Scheme_SchemeType_Int16.htm)|  
[Int32](F_Tessa_Scheme_SchemeType_Int32.htm)|  
[Int64](F_Tessa_Scheme_SchemeType_Int64.htm)|  
[Json](F_Tessa_Scheme_SchemeType_Json.htm)|  
[KnownTypes](F_Tessa_Scheme_SchemeType_KnownTypes.htm)|  
[NullableAnsiString](F_Tessa_Scheme_SchemeType_NullableAnsiString.htm)|  
[NullableAnsiStringFixedLength](F_Tessa_Scheme_SchemeType_NullableAnsiStringFixedLength.htm)|  
[NullableBinary](F_Tessa_Scheme_SchemeType_NullableBinary.htm)|  
[NullableBinaryJson](F_Tessa_Scheme_SchemeType_NullableBinaryJson.htm)|  
[NullableBoolean](F_Tessa_Scheme_SchemeType_NullableBoolean.htm)|  
[NullableByte](F_Tessa_Scheme_SchemeType_NullableByte.htm)|  
[NullableCurrency](F_Tessa_Scheme_SchemeType_NullableCurrency.htm)|  
[NullableDate](F_Tessa_Scheme_SchemeType_NullableDate.htm)|  
[NullableDateTime](F_Tessa_Scheme_SchemeType_NullableDateTime.htm)|  
[NullableDateTime2](F_Tessa_Scheme_SchemeType_NullableDateTime2.htm)|  
[NullableDateTimeOffset](F_Tessa_Scheme_SchemeType_NullableDateTimeOffset.htm)|  
[NullableDecimal](F_Tessa_Scheme_SchemeType_NullableDecimal.htm)|  
[NullableDouble](F_Tessa_Scheme_SchemeType_NullableDouble.htm)|  
[NullableGuid](F_Tessa_Scheme_SchemeType_NullableGuid.htm)|  
[NullableInt16](F_Tessa_Scheme_SchemeType_NullableInt16.htm)|  
[NullableInt32](F_Tessa_Scheme_SchemeType_NullableInt32.htm)|  
[NullableInt64](F_Tessa_Scheme_SchemeType_NullableInt64.htm)|  
[NullableJson](F_Tessa_Scheme_SchemeType_NullableJson.htm)|  
[NullableReferenceAbstract](F_Tessa_Scheme_SchemeType_NullableReferenceAbstract.htm)|
Нельзя указывать тип ReferenceAbstract до того, как колонка добавлена в
таблицу.  
[NullableReferenceTypified](F_Tessa_Scheme_SchemeType_NullableReferenceTypified.htm)|  
[NullableSByte](F_Tessa_Scheme_SchemeType_NullableSByte.htm)|  
[NullableSingle](F_Tessa_Scheme_SchemeType_NullableSingle.htm)|  
[NullableString](F_Tessa_Scheme_SchemeType_NullableString.htm)|  
[NullableStringFixedLength](F_Tessa_Scheme_SchemeType_NullableStringFixedLength.htm)|  
[NullableTime](F_Tessa_Scheme_SchemeType_NullableTime.htm)|  
[NullableUInt16](F_Tessa_Scheme_SchemeType_NullableUInt16.htm)|  
[NullableUInt32](F_Tessa_Scheme_SchemeType_NullableUInt32.htm)|  
[NullableUInt64](F_Tessa_Scheme_SchemeType_NullableUInt64.htm)|  
[NullableXml](F_Tessa_Scheme_SchemeType_NullableXml.htm)|  
[ReferenceAbstract](F_Tessa_Scheme_SchemeType_ReferenceAbstract.htm)|  Нельзя
указывать тип ReferenceAbstract до того, как колонка добавлена в таблицу.  
[ReferenceTypified](F_Tessa_Scheme_SchemeType_ReferenceTypified.htm)|  
[SByte](F_Tessa_Scheme_SchemeType_SByte.htm)|  
[Single](F_Tessa_Scheme_SchemeType_Single.htm)|  
[String](F_Tessa_Scheme_SchemeType_String.htm)|  
[StringFixedLength](F_Tessa_Scheme_SchemeType_StringFixedLength.htm)|  
[Time](F_Tessa_Scheme_SchemeType_Time.htm)|  
[UInt16](F_Tessa_Scheme_SchemeType_UInt16.htm)|  
[UInt32](F_Tessa_Scheme_SchemeType_UInt32.htm)|  
[UInt64](F_Tessa_Scheme_SchemeType_UInt64.htm)|  
[Xml](F_Tessa_Scheme_SchemeType_Xml.htm)|  
## __Методы расширения
[Get](M_Tessa_Extensions_Default_Client_EDS_ComHelper_Get.htm)|  
(Определяется
[ComHelper](T_Tessa_Extensions_Default_Client_EDS_ComHelper.htm))  
---|---  
[GetAvailableCriteria](M_Tessa_Views_Metadata_CriteriaHelper_GetAvailableCriteria.htm)|
Возвращает список доступных критериев для описателя типа данных  
(Определяется [CriteriaHelper](T_Tessa_Views_Metadata_CriteriaHelper.htm))  
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
