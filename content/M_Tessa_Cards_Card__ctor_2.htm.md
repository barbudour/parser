# Card(IStorageObjectProvider) - конструктор
Создаёт экземпляр класса с указанием объекта, предоставляющего доступ к
хранилищу, декоратором для которого является создаваемый объект.
## __Definition
 **Пространство имён:** [Tessa.Cards](N_Tessa_Cards.htm)  
 **Сборка:** Tessa (в Tessa.dll) Версия: 3.6.0.17
C# __Копировать
     public Card(
    	IStorageObjectProvider storageProvider
    )
VB __Копировать
     Public Sub New ( 
    	storageProvider As IStorageObjectProvider
    )
C++ __Копировать
     public:
    Card(
    	IStorageObjectProvider^ storageProvider
    )
F# __Копировать
     new : 
            storageProvider : IStorageObjectProvider -> Card
#### Параметры
storageProvider
[IStorageObjectProvider](T_Tessa_Platform_Storage_IStorageObjectProvider.htm)
     Объект, предоставляющий доступ к хранилищу Dictionary<string, object>, декоратором для которого является создаваемый объект. 
## __См. также
#### Ссылки
[Card - ](T_Tessa_Cards_Card.htm)
[Card - перегрузка](Overload_Tessa_Cards_Card__ctor.htm)
[Tessa.Cards - пространство имён](N_Tessa_Cards.htm)