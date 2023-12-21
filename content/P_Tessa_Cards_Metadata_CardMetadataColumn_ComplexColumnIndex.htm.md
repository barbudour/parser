# CardMetadataColumn.ComplexColumnIndex - свойство
Уникальный в пределах таблицы отсчитываемый от нуля индекс, если текущая
колонка комплексная, или индекс комплексной колонки, в которую включена
текущая физическая колонка, или -1, если текущая физическая колонка не
включена в комплексную колонку.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public short ComplexColumnIndex { get; set; }
VB __Копировать
     Public Property ComplexColumnIndex As Short
    	Get
    	Set
C++ __Копировать
     public:
    property short ComplexColumnIndex {
    	short get ();
    	void set (short value);
    }
F# __Копировать
     member ComplexColumnIndex : int16 with get, set
#### Значение свойства
[Int16](https://learn.microsoft.com/dotnet/api/system.int16)
##  __См. также
#### Ссылки
[CardMetadataColumn - ](T_Tessa_Cards_Metadata_CardMetadataColumn.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
