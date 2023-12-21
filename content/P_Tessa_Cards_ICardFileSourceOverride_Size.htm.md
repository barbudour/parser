# ICardFileSourceOverride.Size - свойство
Текущий размер занятого места в байтах в местоположении. Не заполняется и не
используется системой, возможно использование в расширениях.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     int? Size { get; set; }
VB __Копировать
     Property Size As Integer?
    	Get
    	Set
C++ __Копировать
    property Nullable<int> Size {
    	Nullable<int> get ();
    	void set (Nullable<int> value);
    }
F# __Копировать
     abstract Size : Nullable<int> with get, set
#### Значение свойства
[Nullable](https://learn.microsoft.com/dotnet/api/system.nullable-1)<[Int32](https://learn.microsoft.com/dotnet/api/system.int32)>
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardFileSourceOverride - ](T_Tessa_Cards_ICardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
