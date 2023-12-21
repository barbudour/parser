# ICardFileSourceOverride.Path - свойство
Путь к местоположению. Соответвует имени строки подключения к БД из
конфигурационного файла или полному путь к файловой папке.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     string Path { get; set; }
VB __Копировать
     Property Path As String
    	Get
    	Set
C++ __Копировать
    property String^ Path {
    	String^ get ();
    	void set (String^ value);
    }
F# __Копировать
     abstract Path : string with get, set
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[ICardFileSourceOverride - ](T_Tessa_Cards_ICardFileSourceOverride.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
