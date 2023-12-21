# CardTypeColumn.MaxLength - свойство
Максимальная отображаемая длина колонки в ячейке таблицы. Равна null или нулю,
если ограничения отсутствуют.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int? MaxLength { get; set; }
VB __Копировать
     Public Property MaxLength As Integer?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<int> MaxLength {
    	Nullable<int> get ();
    	void set (Nullable<int> value);
    }
F# __Копировать
     member MaxLength : Nullable<int> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
##  __Заметки
Настройки, связанные с UI.
## __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
