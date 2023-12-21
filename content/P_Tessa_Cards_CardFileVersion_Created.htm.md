# CardFileVersion.Created - свойство
Дата создания версии (изменения файла).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public DateTime Created { get; set; }
VB __Копировать
     Public Property Created As DateTime
    	Get
    	Set
C++ __Копировать
     public:
    property DateTime Created {
    	DateTime get ();
    	void set (DateTime value);
    }
F# __Копировать
     member Created : DateTime with get, set
#### Значение свойства
[DateTime](https://learn.microsoft.com/dotnet/api/system.datetime)
##  __Заметки
Свойство содержит дату создания версии, если была выполнена загрузка версий
методом [LoadFileVersionsAsync(Guid, ListStorage<CardFileVersion>, DbManager,
IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadFileVersionsAsync.htm),
иначе свойство содержит дату изменения файла из таблицы
[Files](F_Tessa_Scheme_Names_Files.htm).
##  __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
