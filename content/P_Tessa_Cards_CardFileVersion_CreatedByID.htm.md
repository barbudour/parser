# CardFileVersion.CreatedByID - свойство
Идентификатор пользователя, создавшего версию (изменившего файл).
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid CreatedByID { get; set; }
VB __Копировать
     Public Property CreatedByID As Guid
    	Get
    	Set
C++ __Копировать
     public:
    property Guid CreatedByID {
    	Guid get ();
    	void set (Guid value);
    }
F# __Копировать
     member CreatedByID : Guid with get, set
#### Значение свойства
[Guid](https://learn.microsoft.com/dotnet/api/system.guid)
##  __Заметки
Свойство содержит идентификатор пользователя, создавшего версию, если была
выполнена загрузка версий методом [LoadFileVersionsAsync(Guid,
ListStorage<CardFileVersion>, DbManager, IValidationResultBuilder,
CancellationToken)](M_Tessa_Cards_ComponentModel_ICardGetStrategy_LoadFileVersionsAsync.htm),
иначе свойство содержит идентификатор пользователя изменившего файл из таблицы
[Files](F_Tessa_Scheme_Names_Files.htm).
##  __См. также
#### Ссылки
[CardFileVersion - ](T_Tessa_Cards_CardFileVersion.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
