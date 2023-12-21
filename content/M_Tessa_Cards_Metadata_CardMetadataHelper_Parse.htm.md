# CardMetadataHelper.Parse - метод
Преобразует объект заданного типа из строкового представления в исходную
форму. Объект должен был быть преобразован в строковую форму методом
[ToString(Object,
CardMetadataRuntimeType)](M_Tessa_Cards_Metadata_CardMetadataHelper_ToString.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object Parse(
    	string valueString,
    	CardMetadataRuntimeType type
    )
VB __Копировать
     Public Shared Function Parse ( 
    	valueString As String,
    	type As CardMetadataRuntimeType
    ) As Object
C++ __Копировать
     public:
    static Object^ Parse(
    	String^ valueString, 
    	CardMetadataRuntimeType type
    )
F# __Копировать
     static member Parse : 
            valueString : string * 
            type : CardMetadataRuntimeType -> Object 
#### Параметры
valueString [String](https://learn.microsoft.com/dotnet/api/system.string)
     Строковое представление объекта, который требуется преобразовать в исходную форму. 
type
[CardMetadataRuntimeType](T_Tessa_Cards_Metadata_CardMetadataRuntimeType.htm)
    Тип объекта, который требуется преобразовать в исходную форму.
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Исходное представление объекта, полученного из заданной строки.
##  __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
