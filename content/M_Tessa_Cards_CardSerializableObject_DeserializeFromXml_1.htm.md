# CardSerializableObject.DeserializeFromXml(String) - метод
Выполняет десериализацию объекта из XML, заданного посредством строки.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromXml(
    	string xmlText
    )
VB __Копировать
     Public Sub DeserializeFromXml ( 
    	xmlText As String
    )
C++ __Копировать
     public:
    void DeserializeFromXml(
    	String^ xmlText
    )
F# __Копировать
     member DeserializeFromXml : 
            xmlText : string -> unit 
#### Параметры
xmlText [String](https://learn.microsoft.com/dotnet/api/system.string)
    XML, заданный посредством строки.
##  __Исключения
[Tessa.Platform.ObjectSealedException]| Произведена попытка изменения объекта,
защищённого от изменений.  
---|---  
##  __См. также
#### Ссылки
[CardSerializableObject - ](T_Tessa_Cards_CardSerializableObject.htm)
[DeserializeFromXml -
перегрузка](Overload_Tessa_Cards_CardSerializableObject_DeserializeFromXml.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
[Tessa.Platform.ObjectSealedException]
