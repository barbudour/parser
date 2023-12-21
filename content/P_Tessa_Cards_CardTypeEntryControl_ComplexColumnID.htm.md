# CardTypeEntryControl.ComplexColumnID - свойство
Идентификатор комплексной колонки, в которой содержится значение поля, или
null, если поле содержится в физической колонке или составлено из нескольких
физических колонок.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? ComplexColumnID { get; set; }
VB __Копировать
     Public Property ComplexColumnID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> ComplexColumnID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member ComplexColumnID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeEntryControl - ](T_Tessa_Cards_CardTypeEntryControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
