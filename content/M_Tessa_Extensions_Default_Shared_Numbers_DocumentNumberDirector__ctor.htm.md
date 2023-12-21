# DocumentNumberDirector - конструктор
Создаёт экземпляр класса с указанием его зависимостей.
## __Definition
 **Пространство имён:**
[Tessa.Extensions.Default.Shared.Numbers](N_Tessa_Extensions_Default_Shared_Numbers.htm)  
 **Сборка:** Tessa.Extensions.Default.Shared (в
Tessa.Extensions.Default.Shared.dll) Версия: 3.6.0.17
C# __Копировать
     public DocumentNumberDirector(
    	IKrTypesCache typesCache,
    	INumberDependencies dependencies
    )
VB __Копировать
     Public Sub New ( 
    	typesCache As IKrTypesCache,
    	dependencies As INumberDependencies
    )
C++ __Копировать
     public:
    DocumentNumberDirector(
    	IKrTypesCache^ typesCache, 
    	INumberDependencies^ dependencies
    )
F# __Копировать
     new : 
            typesCache : IKrTypesCache * 
            dependencies : INumberDependencies -> DocumentNumberDirector
#### Параметры
typesCache
[IKrTypesCache](T_Tessa_Extensions_Default_Shared_Workflow_KrProcess_IKrTypesCache.htm)
    Кэш типов карточек и документов, включённых в типовое решение.
dependencies
[INumberDependencies](T_Tessa_Cards_Numbers_INumberDependencies.htm)
    Объект, содержащий внешние зависимости API номеров.
##  __См. также
#### Ссылки
[DocumentNumberDirector -
](T_Tessa_Extensions_Default_Shared_Numbers_DocumentNumberDirector.htm)
[Tessa.Extensions.Default.Shared.Numbers - пространство
имён](N_Tessa_Extensions_Default_Shared_Numbers.htm)
