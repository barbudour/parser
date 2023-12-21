# TaskSatelliteStoreExtension.NextCardIDKey - свойство
Имя уникального ключа, по которому в ответе на запрос response.Info содержится
идентификатор карточки, которую надо открыть после сохранения сателлита. Если
в ответе на запрос ключ не указан, то после сохранения повторно открывается
сателлит.
## __Definition
 **Пространство имён:**
[Tessa.Cards.Extensions.Templates](N_Tessa_Cards_Extensions_Templates.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     protected abstract string NextCardIDKey { get; }
VB __Копировать
     Protected MustOverride ReadOnly Property NextCardIDKey As String
    	Get
C++ __Копировать
     protected:
    virtual property String^ NextCardIDKey {
    	String^ get () abstract;
    }
F# __Копировать
     abstract NextCardIDKey : string with get
#### Значение свойства
[String](https://learn.microsoft.com/dotnet/api/system.string)
##  __См. также
#### Ссылки
[TaskSatelliteStoreExtension -
](T_Tessa_Cards_Extensions_Templates_TaskSatelliteStoreExtension.htm)
[Tessa.Cards.Extensions.Templates - пространство
имён](N_Tessa_Cards_Extensions_Templates.htm)
