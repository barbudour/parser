# TaskSatelliteGetExtension.VirtualMainCardIDKey - свойство
Имя уникального ключа, по которому в карточке сателлита card.Info содержится
идентификатор основной карточки, если карточка-сателлит была открыта как
виртуальная, т.е. она не существовала на момент загрузки. Если в карточке ключ
не указан, то сателлит уже был создан ранее.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract string VirtualMainCardIDKey { get; }
VB __Копировать
     Protected MustOverride ReadOnly Property VirtualMainCardIDKey As String
    	Get
C++ __Копировать
     protected:
    virtual property String^ VirtualMainCardIDKey {
    	String^ get () abstract;
    }
F# __Копировать
     abstract VirtualMainCardIDKey : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[TaskSatelliteGetExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteGetExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
