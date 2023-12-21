# CardHeader.OperationID - свойство
Идентификатор операции, которая должна быть завершена после выполнения
действий с карточкой, или null, если операция не создавалась.
## __Definition
 **Пространство имён:**
[Tessa.Cards.ComponentModel](N_Tessa_Cards_ComponentModel.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Guid? OperationID { get; set; }
VB __Копировать
     Public Property OperationID As Guid?
    	Get
    	Set
C++ __Копировать
     public:
    property Nullable<Guid> OperationID {
    	Nullable<Guid> get ();
    	void set (Nullable<Guid> value);
    }
F# __Копировать
     member OperationID : Nullable<Guid> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Guid](https://learn.microsoft.com/dotnet/api/system.guid)>
##  __Заметки
Значение по умолчанию null возвращается даже в том случае, если
соответствующий ключ отсутствует в хранилище.
## __См. также
#### Ссылки
[CardHeader - ](T_Tessa_Cards_ComponentModel_CardHeader.htm)
[Tessa.Cards.ComponentModel - пространство
имён](N_Tessa_Cards_ComponentModel.htm)
