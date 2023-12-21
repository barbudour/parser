# CardSerializableObject.DeserializeFromXml(XmlReader) - метод
Выполняет десериализацию объекта и всех его дочерних объектов из элемента XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public void DeserializeFromXml(
    	XmlReader reader
    )
VB __Копировать
     Public Sub DeserializeFromXml ( 
    	reader As XmlReader
    )
C++ __Копировать
     public:
    void DeserializeFromXml(
    	XmlReader^ reader
    )
F# __Копировать
     member DeserializeFromXml : 
            reader : XmlReader -> unit 
#### Параметры
reader
[XmlReader](https://learn.microsoft.com/dotnet/api/system.xml.xmlreader)
    Объект, осуществляющий чтение из сериализованных в XML данных.
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
