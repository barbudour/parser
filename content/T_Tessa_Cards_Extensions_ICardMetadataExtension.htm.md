# ICardMetadataExtension - интерфейс
Расширение, выполняемое при построении метаинформации по типам карточек
[ICardMetadata](T_Tessa_Cards_ICardMetadata.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Extensions](N_Tessa_Cards_Extensions.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public interface ICardMetadataExtension : IExtension
VB __Копировать
     Public Interface ICardMetadataExtension
    	Inherits IExtension
C++ __Копировать
     public interface class ICardMetadataExtension : IExtension
F# __Копировать
     type ICardMetadataExtension = 
        interface
            interface IExtension
        end
Implements
    [IExtension](T_Tessa_Extensions_IExtension.htm)
##  __Методы
[ModifyMetadata](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyMetadata.htm)|
Изменяет метаинформацию по типам карточек после её построения.  
---|---  
[ModifyTypes](M_Tessa_Cards_Extensions_ICardMetadataExtension_ModifyTypes.htm)|
Изменяет типы карточек, по которым затем будет строиться метаинформация.  
##  __См. также
#### Ссылки
[Tessa.Cards.Extensions - пространство имён](N_Tessa_Cards_Extensions.htm)
