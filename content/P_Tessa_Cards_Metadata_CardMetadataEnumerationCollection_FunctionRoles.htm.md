# CardMetadataEnumerationCollection.FunctionRoles - свойство
Функциональные роли заданий. Идентификаторы типовых ролей перечислены в классе
[CardFunctionRoles](T_Tessa_Cards_CardFunctionRoles.htm).
## __Definition
 **Пространство имён:** [Tessa.Cards.Metadata](N_Tessa_Cards_Metadata.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public CardMetadataFunctionRoleCollection FunctionRoles { get; }
VB __Копировать
     Public ReadOnly Property FunctionRoles As CardMetadataFunctionRoleCollection
    	Get
C++ __Копировать
     public:
    property CardMetadataFunctionRoleCollection^ FunctionRoles {
    	CardMetadataFunctionRoleCollection^ get ();
    }
F# __Копировать
     member FunctionRoles : CardMetadataFunctionRoleCollection with get
#### Значение свойства
[CardMetadataFunctionRoleCollection](T_Tessa_Cards_Metadata_CardMetadataFunctionRoleCollection.htm)
##  __Заметки
Значение свойства никогда не равно null.
Значение свойства рекомендуется использовать, если текущий объект защищён от
изменений. В противном случае при каждом обращении к свойству будет
создаваться новый объект.
## __См. также
#### Ссылки
[CardMetadataEnumerationCollection -
](T_Tessa_Cards_Metadata_CardMetadataEnumerationCollection.htm)
[Tessa.Cards.Metadata - пространство имён](N_Tessa_Cards_Metadata.htm)
