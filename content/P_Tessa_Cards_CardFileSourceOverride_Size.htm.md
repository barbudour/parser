# CardFileSourceOverride.Size - свойство
Текущий размер занятого места в байтах в местоположении. Не заполняется и не
используется системой, возможно использование в расширениях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public int? Size { get; set; }
VB __Копировать
     Public Property Size As Integer?
    	Get
    	Set
C++ __Копировать
     public:
    virtual property Nullable<int> Size {
    	Nullable<int> get () sealed;
    	void set (Nullable<int> value) sealed;
    }
F# __Копировать
     abstract Size : Nullable<int> with get, set
    override Size : Nullable<int> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
#### Реализации
[ICardFileSourceOverride.Size](P_Tessa_Cards_ICardFileSourceOverride_Size.htm)  
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardFileSourceOverride - ](T_Tessa_Cards_CardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
