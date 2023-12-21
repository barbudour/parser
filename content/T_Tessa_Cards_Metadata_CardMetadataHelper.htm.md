# CardMetadataHelper - класс
Вспомогательные методы для преобразования и хранения данных карточки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static class CardMetadataHelper
VB __Копировать
     Public NotInheritable Class CardMetadataHelper
C++ __Копировать
     public ref class CardMetadataHelper abstract sealed
F# __Копировать
     [<AbstractClassAttribute>]
    [<SealedAttribute>]
    type CardMetadataHelper = class end
Inheritance
    [Object](https://learn.microsoft.com/dotnet/api/system.object) __ CardMetadataHelper
##  __Методы
[CoerceAfterLoading(Object,
CardMetadataType)](M_Tessa_Cards_Metadata_CardMetadataHelper_CoerceAfterLoading.htm)|
Корректирует при необходимости загруженное из базы данных значение в
соответствии с заданным типом
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).  
---|---  
[CoerceAfterLoading(Object,
SchemeDbType)](M_Tessa_Cards_Metadata_CardMetadataHelper_CoerceAfterLoading_1.htm)|
Корректирует при необходимости загруженное из базы данных значение в
соответствии с заданным типом
[SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm).  
[CoerceBeforeSaving](M_Tessa_Cards_Metadata_CardMetadataHelper_CoerceBeforeSaving.htm)|
Корректирует при необходимости значение перед сохранением в базу данных в
соответствии с заданным типом
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).  
[Convert](M_Tessa_Cards_Metadata_CardMetadataHelper_Convert.htm)|  Преобразует
объект в заданный тип, обеспечивающий возможность хранения объекта в карточке.  
[ConvertToSchemeType](M_Tessa_Cards_Metadata_CardMetadataHelper_ConvertToSchemeType.htm)|
Возвращает объект [SchemeType](T_Tessa_Scheme_SchemeType.htm), который может
разместить данные указанного объекта
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).  
[ConvertToSectionType](M_Tessa_Cards_Metadata_CardMetadataHelper_ConvertToSectionType.htm)|  
[CreateCardMetadataAsync](M_Tessa_Cards_Metadata_CardMetadataHelper_CreateCardMetadataAsync.htm)|
Создаёт метаинформацию по типам карточек.  
[CreateForTypeAsync](M_Tessa_Cards_Metadata_CardMetadataHelper_CreateForTypeAsync.htm)|
Выполняет построение выборки из метаинформации, относящейся только к заданному
типу карточек.  
[GetDefaultValidValue](M_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValidValue.htm)|
Возвращает значение по умолчанию для заданной физической колонки, которое
может быть размещено в карточке и всегда является валидным при сохранении. Для
колонок, не допускающих Null и не имеющих значения по умолчанию, возвращается
значение по умолчанию для типа этой колонки.  
[GetDefaultValue(CardMetadataType)](M_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValue.htm)|
Возвращает значение по умолчанию для сохранения в карточке, доступное для
заданного типа
[CardMetadataType](T_Tessa_Cards_Metadata_CardMetadataType.htm).  
[GetDefaultValue(SchemePhysicalColumn)](M_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValue_2.htm)|
Возвращает значение по умолчанию для заданной физической колонки, которое
может быть размещено в карточке. Для колонок, не допускающих Null и не имеющих
значения по умолчанию, возвращается Null.  
[GetDefaultValue(SchemeDbType,
Boolean)](M_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValue_1.htm)|
Возвращает значение по умолчанию для сохранения в карточке, доступное для
заданного типа [SchemeDbType](T_Tessa_Platform_Data_SchemeDbType.htm).  
[GetDefaultValueFunc](M_Tessa_Cards_Metadata_CardMetadataHelper_GetDefaultValueFunc.htm)|
Возвращает функцию, которая для заданного режима создания карточки получает
значение по умолчанию для указанной в параметре колонки
[CardMetadataColumn](T_Tessa_Cards_Metadata_CardMetadataColumn.htm).  
[GetMetadataRuntimeType(SchemeType)](M_Tessa_Cards_Metadata_CardMetadataHelper_GetMetadataRuntimeType_1.htm)|
Возвращает способ представления в карточке данных заданного типа.  
[GetMetadataRuntimeType(Type)](M_Tessa_Cards_Metadata_CardMetadataHelper_GetMetadataRuntimeType.htm)|
Возвращает способ представления в карточке объекта заданного типа.  
[GetRuntimeType](M_Tessa_Cards_Metadata_CardMetadataHelper_GetRuntimeType.htm)|
Возвращает тип объекта, представленного в карточке заданным способом.  
[HasLength](M_Tessa_Cards_Metadata_CardMetadataHelper_HasLength.htm)|
Возвращает признак того, что заданный тип имеет длину.  
[HasLength15](M_Tessa_Cards_Metadata_CardMetadataHelper_HasLength15.htm)|
Возвращает признак того, что заданный тип имеет длину, которая умещается в 15
бит и может быть сериализована как 16-битное знаковое число.  
[HasPrecision](M_Tessa_Cards_Metadata_CardMetadataHelper_HasPrecision.htm)|
Возвращает признак того, что заданный тип имеет точность.  
[HasScale](M_Tessa_Cards_Metadata_CardMetadataHelper_HasScale.htm)|
Возвращает признак того, что заданный тип имеет масштаб.  
[Parse](M_Tessa_Cards_Metadata_CardMetadataHelper_Parse.htm)|  Преобразует
объект заданного типа из строкового представления в исходную форму. Объект
должен был быть преобразован в строковую форму методом [ToString(Object,
CardMetadataRuntimeType)](M_Tessa_Cards_Metadata_CardMetadataHelper_ToString.htm).  
[Read](M_Tessa_Cards_Metadata_CardMetadataHelper_Read.htm)|  Выполняет чтение
объекта заданного типа данных из байтового потока. Объект должен был быть
записан в байтовый поток посредством метода [Write(BinaryWriter, Object,
CardMetadataType,
Nullable<Boolean>)](M_Tessa_Cards_Metadata_CardMetadataHelper_Write.htm).  
[ToString](M_Tessa_Cards_Metadata_CardMetadataHelper_ToString.htm)|
Преобразует объект заданного типа в строку. Объект может быть преобразован в
исходную форму методом [Parse(String,
CardMetadataRuntimeType)](M_Tessa_Cards_Metadata_CardMetadataHelper_Parse.htm).  
[Write](M_Tessa_Cards_Metadata_CardMetadataHelper_Write.htm)|  Выполняет
запись объекта заданного типа данных в байтовый поток. Объект может быть
прочитан из байтового потока посредством метода [Read(BinaryReader,
CardMetadataType,
Nullable<Boolean>)](M_Tessa_Cards_Metadata_CardMetadataHelper_Read.htm).  
## __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
