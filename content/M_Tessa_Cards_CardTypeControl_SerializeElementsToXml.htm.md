# CardTypeControl.SerializeElementsToXml - метод
Выполняет сериализацию всех дочерних объектов для текущего объекта в элементы
XML.
##  __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected override void SerializeElementsToXml(
    	XmlWriter writer
    )
VB __Копировать
     Protected Overrides Sub SerializeElementsToXml ( 
    	writer As XmlWriter
    )
C++ __Копировать
     protected:
    virtual void SerializeElementsToXml(
    	XmlWriter^ writer
    ) override
F# __Копировать
     abstract SerializeElementsToXml : 
            writer : XmlWriter -> unit 
    override SerializeElementsToXml : 
            writer : XmlWriter -> unit 
#### Параметры
writer
[XmlWriter](https://learn.microsoft.com/dotnet/api/system.xml.xmlwriter)
    Объект, выполняющий запись сериализованных данных в XML.
##  __См. также
#### Ссылки
[CardTypeControl - ](T_Tessa_Cards_CardTypeControl.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)
