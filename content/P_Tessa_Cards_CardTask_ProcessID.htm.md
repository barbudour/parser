# CardTask.ProcessID - свойство
Идентификатор бизнес-процесса, к которому относится запись в истории заданий,
которая будет добавлена для задания, или null, если запись не относится к
бизнес-процессу. Свойство следует устанавливать перед изменением или
завершением задания, для которого будет добавлена запись в истории. Свойство
не изменяется при изменении записи в истории. По умолчанию значение равно
null.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? ProcessID { get; set; }
VB __Копировать
     Public Property ProcessID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> ProcessID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member ProcessID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __См. также
#### Ссылки
[CardTask - ](T_Tessa_Cards_CardTask.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
