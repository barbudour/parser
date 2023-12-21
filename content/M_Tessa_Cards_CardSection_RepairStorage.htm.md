# CardSection.RepairStorage - метод
Исправляет хранилище объекта, типы в котором установлены некорректно, после
десериализации из JSON. Возвращает признак того, что при исправлении в объекте
были изменения.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public bool RepairStorage(
    	CardMetadataSection metadataSection
    )
VB __Копировать
     Public Function RepairStorage ( 
    	metadataSection As CardMetadataSection
    ) As Boolean
C++ __Копировать
     public:
    bool RepairStorage(
    	CardMetadataSection^ metadataSection
    )
F# __Копировать
     member RepairStorage : 
            metadataSection : CardMetadataSection -> bool 
#### Параметры
metadataSection
[CardMetadataSection](T_Tessa_Cards_Metadata_CardMetadataSection.htm)
    Метаинформация по исправляемой секции.
#### Возвращаемое значение
[Boolean](https://learn.microsoft.com/dotnet/api/system.boolean)  
true, если при исправлении в объект были внесены изменения; false в противном
случае.
## __См. также
#### Ссылки
[CardSection - ](T_Tessa_Cards_CardSection.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
