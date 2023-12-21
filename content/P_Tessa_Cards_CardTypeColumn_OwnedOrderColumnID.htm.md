# CardTypeColumn.OwnedOrderColumnID - свойство
Идентификатор колонки в дочерней секции, задающей порядок отображения дочерних
строк, или null, если текущий объект не связан с дочерней секцией или дочерняя
секция не упорядочена.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? OwnedOrderColumnID { get; set; }
VB __Копировать
     Public Property OwnedOrderColumnID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> OwnedOrderColumnID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member OwnedOrderColumnID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardTypeColumn - ](T_Tessa_Cards_CardTypeColumn.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
