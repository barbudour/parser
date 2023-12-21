# ICardMetadataBinder - интерфейс
Объект, осуществляющий действия с карточкой [Card](T_Tessa_Cards_Card.htm),
требующие наличие метаинформации
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm), такие как удаление строк
коллекционных секций с учётом всех дочерних строк.
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMetadataBinder
VB __Копировать
     Public Interface ICardMetadataBinder
C++ __Копировать
     public interface class ICardMetadataBinder
F# __Копировать
     type ICardMetadataBinder = interface end
##  __Методы
[RemoveRowAsync](M_Tessa_Cards_Metadata_ICardMetadataBinder_RemoveRowAsync.htm)|
Выполняет удаление указанной строки из коллекционной или древовидной секции с
заданным именем, при этом учитывается возможное наличие строк в дочерних
секциях.  
---|---  
## __См. также
#### Ссылки
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
