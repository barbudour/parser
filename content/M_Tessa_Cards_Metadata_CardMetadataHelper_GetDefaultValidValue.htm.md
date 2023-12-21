# CardMetadataHelper.GetDefaultValidValue - метод
Возвращает значение по умолчанию для заданной физической колонки, которое
может быть размещено в карточке и всегда является валидным при сохранении. Для
колонок, не допускающих Null и не имеющих значения по умолчанию, возвращается
значение по умолчанию для типа этой колонки.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public static Object GetDefaultValidValue(
    	SchemePhysicalColumn column
    )
VB __Копировать
     Public Shared Function GetDefaultValidValue ( 
    	column As SchemePhysicalColumn
    ) As Object
C++ __Копировать
     public:
    static Object^ GetDefaultValidValue(
    	SchemePhysicalColumn^ column
    )
F# __Копировать
     static member GetDefaultValidValue : 
            column : SchemePhysicalColumn -> Object 
#### Параметры
column [SchemePhysicalColumn](T_Tessa_Scheme_SchemePhysicalColumn.htm)
     Физическая колонка, информация из которой используется для получения значения по умолчанию. 
#### Возвращаемое значение
[Object](https://learn.microsoft.com/dotnet/api/system.object)  
Значение по умолчанию для заданной физической колонки, которое может быть
размещено в карточке и всегда является валидным при сохранении.
## __См. также
#### Ссылки
[CardMetadataHelper - ](T_Tessa_Cards_Metadata_CardMetadataHelper.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
